from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly
from .models import Course, Topic, Unit, TopicPhoto, \
    Example, ExamplePhoto, ExampleNumber
from .serializers import CourseListSerializer, CourseRetrieveSerializer, TopicRetrieveSerializer, \
    TopicListSerializer, UnitRetrieveSerializer, UnitListSerializer


class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CourseRetrieveSerializer(instance)
        return Response(serializer.data)


class UnitViewset(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitListSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UnitRetrieveSerializer(instance)
        return Response(serializer.data)


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TopicRetrieveSerializer(instance)
        return Response(serializer.data)




