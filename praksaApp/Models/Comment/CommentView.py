from .CommentModel import Comment
from .CommentSerializer import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def CommentList(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(Comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def CommentDetail(request, id):
    
    try:
        comment = Comment.objects.get(commentId = id)
    except Comment.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        comment.isActive = False
        serializer = CommentSerializer(comment)
        serializer.save()
        