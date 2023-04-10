from rest_framework.serializers import ModelSerializer
from course.models import Course , Unit , Topic


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

