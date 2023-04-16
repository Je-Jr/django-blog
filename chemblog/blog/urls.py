from django.urls import path
from .views import IndexView, ArticleDetailView, AddPostView, UpdatePostView
# from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post')
]