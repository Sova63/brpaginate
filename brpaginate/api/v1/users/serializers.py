from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer,CharField


class ObtainTokenSerializer(ModelSerializer):
	username = CharField(max_length=150,validators=[])
	class Meta:
		model = get_user_model()
		fields = (
			'username',
			'password'
		)