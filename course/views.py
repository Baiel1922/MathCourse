from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from course.models import Course ,Topic , Unit
from course.serializers import CourseSerializer ,TopicSerializer , UnitSerializer

from MathCourse.course.permissions import IsAdminOrReadOnly


class CourseViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly ,)


class UnitViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAdminOrReadOnly)


class TopicViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    queryset = Topic.objects.all()
    serializer = UnitSerializer
    permission_classes = (IsAdminOrReadOnly ,)







