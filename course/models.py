from django.db import models



class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title




class Unit(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)

    def __str__(self):
        return f' Unit: {self.title} | Category: {self.course.title}'


class Topic(models.Model):
    theory = models.TextField(max_length=800)
    example = models.TextField(max_length=800)
    daily_example = models.TextField(max_length=800)
    image = models.ImageField(upload_to='course_images')
    unit = models.ForeignKey(Unit , on_delete=models.CASCADE)


    def __str__(self):
        return f' Unit: {self.theory} | Category: {self.unit.title}'
