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
        try:
            comments = Comment.objects.filter(video=video_id)
        except ValueError:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
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

    # delete comment
    def delete(self,request,video_id, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except ValueError:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        deleted_comment = CommentSerializer(comment)
        comment.delete()
        return Response(deleted_comment.data, status=status.HTTP_200_OK)



class CommentReview(APIView):

    # like or dislike
    def put(self, request, video_id, comment_id, action):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except ValueError:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
        if action == 'like':
            comment.likes += 1
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif action == 'dislike':
            comment.dislikes += 1
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)




