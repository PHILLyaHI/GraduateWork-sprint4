from django.shortcuts import render
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from api.serializers import *


class VideoUserWritePermission(BasePermission):
    message = "Editing Videos is only for Author"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, pk, format=None):
       instance = self.get_object()
       instance.is_active = False
       instance.save()
       return Response(status=status.HTTP_204_NO_CONTENT)


class VideoViewset(viewsets.ModelViewSet, VideoUserWritePermission):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [VideoUserWritePermission]

    def destroy(self, request, pk, format=None):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, pk, format=None):
       instance = self.get_object()
       instance.is_active = False
       instance.save()
       return Response(status=status.HTTP_204_NO_CONTENT)
