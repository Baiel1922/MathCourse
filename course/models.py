from django.db import models



class Course(models.Model):
    title = models.CharField(max_length=250, unique=True, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title




class Unit(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")

    def __str__(self):
        return f'{self.title} | course: {self.course.title}'


class Topic(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    text = models.TextField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return f'{self.title}'

class TopicPhoto(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="topic_photos")

    def __str__(self):
        return f'{self.topic}'

class Example(models.Model):
    text = models.TextField(null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="examples")

    def __str__(self):
        return f'{self.text}'


class ExamplePhoto(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="example_photos")

    def __str__(self):
        return f'photo of {self.example}'

class ExampleNumber(models.Model):
    example = models.ForeignKey(Example, on_delete=models.CASCADE, related_name="numbers")
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'numbers of {self.example}'