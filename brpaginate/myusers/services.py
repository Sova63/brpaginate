from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


def create_token(request, username, password):
	user = authenticate(request, username=username, password=password)
	if not user:
		return

	return Token.objects.create(user=user).key
