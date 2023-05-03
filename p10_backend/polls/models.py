import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.BooleanField)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_true = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.question} - {self.choise_text} - {self.is_true}"


