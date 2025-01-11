from rest_framework import serializers
from mypaginate.models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = (
			'id','title','created_at'
		)

class ArticlesDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = (
			'id','title','content','created_at'
		)