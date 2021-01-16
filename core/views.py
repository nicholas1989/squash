from django.http import JsonResponse
from django.shortcuts import render
from .models import Post
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import PostSerializer
from rest_framework import generics
from rest_framework import mixins

# Create your views here.
class TestView(APIView):
    
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        qs = Post.object.all()
        post = qs.first()
        #serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    





