from django.shortcuts import render
from rest_framework import viewsets

from account.permission import IsActivePermission
from group.models import Group, GroupStudent
from group.serializers import GroupSerializers, GroupStudentSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [IsActivePermission, ]

class GroupStudentViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializers
    permission_classes = [IsActivePermission, ]