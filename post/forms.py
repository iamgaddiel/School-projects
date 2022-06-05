from django import forms

from post.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']