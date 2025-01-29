from django.urls import path
from api.v1.news.views import ArticlesApiListView,ArticlesDetailView,CreateCommentApi,RetrieveUpdateCommentView

from api.v1.users.views import ObtainTokenApi

urlpatterns = [
    path('articles/', ArticlesApiListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticlesDetailView.as_view(), name='article-detail'),
    path('comments/', CreateCommentApi.as_view(), name='comment-create-api'),
    path('comments/<int:pk>/', RetrieveUpdateCommentView.as_view(), name='comment-update-retrieve-api'),
    path('auth/obtain-token/', ObtainTokenApi.as_view(), name='obtain-token-api')
]