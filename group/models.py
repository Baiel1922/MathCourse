from django.db import models

from account.models import User
from course.models import Course


class Group(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')

class GroupStudent(models.Model):
    points = models.IntegerField()
    score = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_students')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_students')

