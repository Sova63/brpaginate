from django.urls import path
from .views import *

urlpatterns = [
    path('', article_list, name='article_list'),
    #path('article/<int:pk>/', article_detail, name='article_detail'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:article_id>/add_comment', create_comment, name='article-add-comment')
]