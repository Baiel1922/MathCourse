from django.db import models
from course.models import Topic
from account.models import User
class Quiz(models.Model):
    title = models.CharField(max_length=500, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="quizes")

class Question(models.Model):
    text = models.CharField(max_length=500, unique=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

class Answer(models.Model):
    text = models.CharField(max_length=500, unique=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="submissions")
    answers = models.ManyToManyField(Answer)
    point = models.IntegerField()
