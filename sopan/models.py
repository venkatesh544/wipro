from django.db import models


class Python(models.Model):
    heading = models.TextField(max_length=2000)
    code = models.TextField(max_length=20000)

    def __str__(self):
        return self.heading


class Java(models.Model):
    questions = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)


class Save(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')


    def __str__(self):
        return self.name


class Intel(models.Model):
    heading = models.TextField(max_length=2000)
    code = models.TextField(max_length=20000)

    def __str__(self):
        return self.heading
