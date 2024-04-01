from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.views import APIView

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        models.BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    lookup_field = 'pk'


class BlogPostList(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title','')

        if title:
            posts = models.BlogPost.objects.filter(title__icontains=title)
        else:
            posts = models.BlogPost.objects.all()
        
        serializer = serializers.BlogPostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)