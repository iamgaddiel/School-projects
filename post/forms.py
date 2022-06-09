from django import forms

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
