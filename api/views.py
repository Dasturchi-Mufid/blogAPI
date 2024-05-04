from post import models
from . import serializers
from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostList(ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    # permission_classes = permissions.IsAdminUser,
    # authentication_classes = JWTAuthentication,

    def get(self, request, *args, **kwargs):
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = serializers.PostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
