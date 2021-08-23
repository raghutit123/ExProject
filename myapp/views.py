from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializer,CommentsSerializer
from .models import Post,Comments

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List': '/list/',
        'Detail View': '/detail/<int:id>/',
        'Create': '/create/',
        'Update': '/update/<int:id>/',
        'Delete': '/delete/<int:id>/'
    }
    return Response(api_urls);

@api_view(['GET'])
def ShowAll(request):
    post = Post.objects.all()
    serializer = PostSerializer(post,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowSingle(request,pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreatePost(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdatePost(request,pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def DeletePost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response("Items delete successfully")

@api_view(['GET'])
def CommentAll(request):
    comments = Comments.objects.all()
    serializer = CommentsSerializer(comments,many=True)
    return Response(serializer.data)