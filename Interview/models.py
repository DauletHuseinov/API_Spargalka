from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    question = models.TextField(max_length=255)
    short_answer = models.CharField(max_length=255)
    answer = models.TextField()
    importance = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
