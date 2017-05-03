from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework.renderers import JSONRenderer

from users.serializers import UserSerializer


class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_users = serializer.data
        renderer = JSONRenderer()
        json_users = renderer.render(serialized_users)
        return HttpResponse(json_users)

    def post(self, request):
        pass
