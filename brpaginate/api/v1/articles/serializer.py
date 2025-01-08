from rest_framework import serializers

from mypaginate.models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = (
			'title','content','created_at'
		)