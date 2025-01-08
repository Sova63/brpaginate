from django.urls import path
from api.v1.articles.views import ArticlesApiView


urlpatterns = [
    path('articles/', ArticlesApiView.as_view(), name='article_list_new'),
    #path('article/<int:pk>/', views.article_detail, name='article_detail'),
]