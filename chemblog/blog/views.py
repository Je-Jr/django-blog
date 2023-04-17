from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

# Create your views here.

# def index(request):
#     return render(request, 'blog/index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['title']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = UpdatePostForm
    # fields = ['title', 'author', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('index')