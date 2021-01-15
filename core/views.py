from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import PostSerializer

# Create your views here.
class TestView(APIView):
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
