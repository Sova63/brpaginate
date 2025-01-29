from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from myusers.services import create_token
from api.v1.users.serializers import ObtainTokenSerializer


class ObtainTokenApi(APIView):
	serializer_class = ObtainTokenSerializer


	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		token = create_token(request, serializer.data['username'], serializer.data['password'])
		if not token:
			raise AuthenticationFailed(detail='No user')
		return Response(dict(token=token))