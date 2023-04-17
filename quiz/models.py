from django.db import models
from course.models import Topic

class Quiz(models.Model):
    title = models.CharField(max_length=500, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="quizes")

    def __str__(self):
        return f'{self.title} - {self.topic}'

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return f'{self.quiz} - {self.text}'

class Answer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text} - {self.is_correct}'

# class Submission(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="submissions")
#     answers = models.ManyToManyField(Answer)
#
#     def __str__(self):
#         return f'{self.quiz}'
