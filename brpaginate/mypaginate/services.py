from .models import Article,Comment

def get_comments_for_article(article_id):
	return Comment.objects.filter(article_id=article_id)