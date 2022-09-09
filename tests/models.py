from django.db import models


class Questions(models.Model):
    text = models.CharField(max_length=500)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.IntegerField(default=None)


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    questions = models.ManyToManyField(Questions, default=None)


class Predmeti(models.Model):
    title = models.CharField(max_length=100)


