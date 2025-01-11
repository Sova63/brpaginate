from django.contrib import admin
from .models import *
#admin.site.register(Article)
#admin.site.register(Comment)

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
	list_display = (
		'title',
		'content',
		'created_at'
	)

@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
	list_display = (
		'article',
		'user',
		'is_anon',
		'text',
		'created_at'
	)