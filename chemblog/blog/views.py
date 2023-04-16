from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, UpdatePostForm

# Create your views here.

# def index(request):
#     return render(request, 'blog/index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'

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
