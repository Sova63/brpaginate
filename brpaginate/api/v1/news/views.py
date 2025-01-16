from mypaginate.models import Article,Comment
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from api.v1.news.serializer import ArticlesListSerializer, ArticlesDetailSerializer,CommentApiSerializer




class ArticlesApiListView(ListAPIView):
	serializer_class = ArticlesListSerializer
	queryset = Article.objects.all()


class ArticlesDetailView(RetrieveAPIView):
	serializer_class = ArticlesDetailSerializer
	queryset = Article.objects.all()


class CreateCommentApi(CreateAPIView):#1
	serializer_class = CommentApiSerializer


class RetrieveUpdateCommentView(RetrieveUpdateAPIView):
	serializer_class = CommentApiSerializer
	queryset = Comment.objects.all()