from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment_text', 'parent', 'likes', 'dislikes', 'timestamp', 'video']

    def create_reply(self, parent, validated_data):
        reply = Comment
        reply.parent = parent.id
        reply.comment_text = validated_data.get('comment_text', reply.comment_text)
        reply.video = validated_data.get('video', reply.video)
        reply.save()
        return reply
