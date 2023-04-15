from django.urls import path
from .views import IndexView
# from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index')
]