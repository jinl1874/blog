from django.shortcuts import render, get_object_or_404
# from hitcount.models import HitCount
# from hitcount.views import HitCountDetailView, HitCountMixin
from django.db.models import Count
from comment.forms import CommentForm
from . import models

# Create your views here.


# 记录点击次数
# hit_count = HitCount.objects.get_for_object(node)
# hit_response = HitCountMixin.hit_count(request, hit_count)

# context = {
#     'object': node,
# }

# context.update(hit_count_response_asdict())

# 获取各个类别下的数目
cate_num = models.Category.objects.annotate(art_num=Count('article'))


def index(request):
    # 获取所有文章和分类
    articles = models.Article.objects.all()
    # cate_list = models.Category.objects.all()
    articles = articles.order_by('-last_edit_time')
    return render(request, 'blog/index.html', {'articles': articles, 'cate_num': cate_num})


def article_page(request, article_id):
    try:
        article_id = int(article_id)
    except ValueError:
        return render(request, 'blog/404.html', {'error': 'ValueError'})
    article = get_object_or_404(models.Article, pk=article_id)
    # 每次访问过后阅读数都会加1
    article.times += 1
    article.save()

    form = CommentForm()

    # 使用的是article，不是models.Article
    comment_list = article.comment_set.all()
    context = {
        'article': article,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blog/article.html', context=context)


# class ArticleCountHitDetailView(HitCountDetailView):
    # model = models.Article
    # count_hit = True


def search(request):
    error = ''
    if 'q' in request.GET:
        q = request.GET
        if not q['q']:
            # print(q)
            error = "Please enter a search term!"
        else:
            # 取到的 q 是一个字典,所以需要取出来
            articles = models.Article.objects.filter(title__icontains=q['q'])
            articles = articles.order_by('-last_edit_time')
            return render(request, 'blog/index.html', {'query': q, 'articles': articles, 'cate_num': cate_num})
    return render('blog/index.html', {'error': error})


def category(request, cate_name):
    articles = models.Article.objects.filter(cate_name__name=cate_name)
    return render(request, 'blog/index.html', {'articles': articles, 'cate_name': cate_name, 'cate_num': cate_num})


def egg(request):
    return render(request, 'blog/egg.html')
