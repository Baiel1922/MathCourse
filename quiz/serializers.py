from rest_framework.serializers import ModelSerializer
from .models import Quiz, Question, Answer


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['questions'] = QuestionSerializer(instance.questions.all(), many=True).data
        return representation


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answers'] = AnswerSerializer(instance.answers.all(), many=True).data
        return representation


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


# class SubmissionSerializer(ModelSerializer):
#     class Meta:
#         model = Submission
#         fields = '__all__'