from rest_framework import response, request

from rest_framework.authtoken.models import Token

from rest_framework.views import APIView

from django.contrib.auth.models import User

from .models import Student

class GetToken(APIView):
    def get(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)
        user = User.objects.get(username=username, password=password)

        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return response.Response({'ok': token.key}, status=206)