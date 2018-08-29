from django import forms

from article.models import Comment, Article


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content','article']    #必须有外键article 与文章进行关联