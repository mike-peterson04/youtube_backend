from django.shortcuts import render
from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CommentSerializer
# Create your views here.


class VideoComment(APIView):
    # retrieve all comments for a video
    def get(self, request, video_id):
        comments = Comment.objects.filter(video=video_id)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # post new comment to a video
    def post(self, request, video_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentActions(APIView):

    # post reply
    def post(self, request, video_id, comment_id):

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,comment_id):

        comment = Comment.objects.get(pk=comment_id)



