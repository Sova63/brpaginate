from django.views import View
from django.http import JsonResponse
from mypaginate.models import Article

class ArticlesApiView(View):

	def get(self, request, *args, **kwargs):
		articles = Article.objects.all()
		return JsonResponse(dict(articles=[
			dict(title=article.title,content=article.content) for article in articles
		]))
