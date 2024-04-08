from . import serializers
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from . import permissions
from . import models

class PostViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuhorOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


