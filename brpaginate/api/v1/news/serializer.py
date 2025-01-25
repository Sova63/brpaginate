from django.contrib.auth import get_user_model
from rest_framework import serializers
from mypaginate.models import Article, Comment
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer


class ArticlesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = (
			'id',
			'title',
			'created_at'
		)

class CommentSerializer(serializers.ModelSerializer):
	user = PrimaryKeyRelatedField(queryset=get_user_model().objects.all(),default=CurrentUserDefault())
	class Meta:
		model = Comment
		fields = (
			'id',
			'user',
			'article',
			'text'
		)

class ArticlesDetailSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(many=True)
	class Meta:
		model = Article
		fields = (
			'id',
			'title',
			'content',
			'created_at',
			'comments'
		)


class ArticleSerializer(ModelSerializer):
	class Meta:
		model = Article
		fields = (
			'id',
			'title',
			'created_at'
		)

class CommentApiSerializer(ModelSerializer):#1
	class Meta:
		model = Comment
		fields = (
			'id',
			'user',
			'article',
			'text',
		)