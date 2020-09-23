from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .models import Comment
from .forms import CommentForm


# Create your views here.


def art_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            comment = Comment(name=name, email=email, content=content)
            comment.article = article
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            return render(request, 'blog/article.html', {
                'article': article,
                'form': form,
                'comment_list': comment_list,
            })
    return redirect(article)
