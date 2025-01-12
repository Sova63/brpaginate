from rest_framework import serializers
from mypaginate.models import Article, Comment



class ArticlesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = (
			'id','title','created_at'
		)

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = (
			'id',
			'article',
			'text'
		)

class ArticlesDetailSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(many=True)
	class Meta:
		model = Article
		fields = (
			'id','title','content','created_at','comments'
		)

