from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from requests import request
from .models import Post
from .forms import PostCreateForm


# Create your views here.
class PostFeed(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/post_feed.html'

class CreatePost(CreateView):
    form_class = PostCreateForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('core:feed')

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)