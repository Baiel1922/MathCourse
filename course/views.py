from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from course.models import Course ,Topic , Unit
from course.serializers import CourseSerializer ,TopicSerializer , UnitSerializer




@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def unit(request):
    units = Unit.objects.all()
    serializer = UnitSerializer(units , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def topic(request):
    topics = Topic.objects.all()
    serializer = UnitSerializer(topics , many=True)
    return Response(serializer.data)




