from rest_framework import serializers
import CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel.Comment
        fields = '__all__'