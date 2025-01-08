from django.views import View
from django.http import JsonResponse
from mypaginate.models import Article
from rest_framework.generics import ListAPIView

from api.v1.articles.serializer import ArticlesListSerializer


class ArticlesApiView(ListAPIView):
	serializer_class = ArticlesListSerializer
	queryset = Article.objects.all()