from rest_framework.serializers import ModelSerializer
from .models import Course, Unit, Topic, Example, \
    TopicPhoto, ExamplePhoto, ExampleNumber
from quiz.serializers import QuizSerializer

class CourseListSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['units'] = UnitListSerializer(instance.units.all(), many=True).data

        return representation

class UnitListSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['topics'] = TopicListSerializer(instance.topics.all(), many=True).data

        return representation

class TopicListSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class TopicRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['photos'] = TopicPhotoSerializer(instance.photos.all(), many=True).data
        representation['examples'] = ExampleSerializer(instance.examples.all(), many=True).data
        representation['quizes'] = QuizSerializer(instance.quizes.all(), many=True).data

        return representation

class TopicPhotoSerializer(ModelSerializer):
    class Meta:
        model = TopicPhoto
        fields = '__all__'

class ExampleSerializer(ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['example_photos'] = ExamplePhotoSerializer(instance.photos.all(), many=True).data
        representation['example_numbers'] = ExampleNumberSerializer(instance.numbers.all(), many=True).data
        return representation

class ExamplePhotoSerializer(ModelSerializer):
    class Meta:
        model = ExamplePhoto
        fields = '__all__'

class ExampleNumberSerializer(ModelSerializer):
    class Meta:
        model = ExampleNumber
        fields = '__all__'

