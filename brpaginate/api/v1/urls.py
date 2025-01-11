from django.urls import path
from api.v1.news.views import ArticlesApiListView,ArticlesDetailView


urlpatterns = [
    #path('articles/', ArticlesApiListView.as_view(), name='article_list'),
    #path('articles/<int:pk>/', ArticlesDetailView.as_view(), name='article_detail')
]