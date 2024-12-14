from django.contrib import admin
from .models import Article



class ArticlelAdmin(admin.ModelAdmin):
	list_display = ('title','content','created_at')
	search_fields = ('title','content')
	list_filter = ('title',)
	ordering = ('title',)

admin.site.register(Article,ArticlelAdmin)