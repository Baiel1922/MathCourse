from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from account.permission import IsActivePermission
from group.models import Group, GroupStudent
from group.serializers import GroupSerializers, GroupStudentSerializers
from account.permission import IsAuthorPermission

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)




class GroupStudentViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializers
    permission_classes = [IsActivePermission, ]

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(student=user)
        return queryset