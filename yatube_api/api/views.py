from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer
from api.permission import OnlyAuthorHasPerm


class PostViewSet(viewsets.ModelViewSet):
    ''' Позволяет просматривать, создавать, редактировать и удалять посты. '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        OnlyAuthorHasPerm,
    )  # Требуем аутентификацию пользователя для доступа к эндпоинтам

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )  # Добавление пользователя как автора при создании объектов


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    ''' Позволяет просматривать информацию о группах. '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    ''' Чтения, создания, обновления и удаления комментариев к постам. '''
    permission_classes = (OnlyAuthorHasPerm,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
