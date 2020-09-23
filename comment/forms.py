
from django import forms

from .models import Comment


# class CommentForm(forms.Form):
class CommentForm(forms.ModelForm):
    # widget是美化输入框的
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Name'}
            )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
            )
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Comment', 'row': 3}
            )

    )
    class Meta:
            model = Comment
            fields = ['name', 'email','content']
