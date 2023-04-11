from django.db import models

from account.models import User
from course.models import Course


class Group(models.Model):
    title = models.CharField()
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class GroupStudent(models.Model):
    points = models.IntegerField()
    score = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)