from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# def index(request):
#     return render(request, 'blog/index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'