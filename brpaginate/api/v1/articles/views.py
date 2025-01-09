from mypaginate.models import Article
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.v1.articles.serializer import ArticlesListSerializer, ArticlesDetailSerializer


class ArticlesApiListView(ListAPIView):
	serializer_class = ArticlesListSerializer
	queryset = Article.objects.all()


class ArticlesDetailView(RetrieveAPIView):
	serializer_class = ArticlesDetailSerializer
	queryset = Article.objects.all()