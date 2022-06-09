from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from requests import request
from .models import Comment, Post
from .forms import CommentCreationForm, PostCreateForm


# Create your views here.
class PostFeed(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/post_feed.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context

class CreatePost(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post:feed')

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

class PersonalPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/personal_post.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user)
        return context

def delete_post(request, id):
    Post.objects.get(id=id).delete()
    return redirect('post:personal_post')


# ----------------------------------- [ Create Comment ]--------------------------------
def create_comment(request):
    if request.method == 'POST':
        c_form = CommentCreationForm(request.POST)
        c_form.instance.user = request.user
        c_form.instance.post = Post.objects.get(id=request.POST.get('post'))
        if c_form.is_valid(): 
            c_form.save()
        else:
            print(c_form.errors)
    return redirect('post:feed')
