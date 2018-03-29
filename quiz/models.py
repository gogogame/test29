from django.db import models

# Question to ask answer only True or False
class Question(models.Model):
    question_text = models.CharField(max_length=200)


# Possible answer True or False, include amount answered
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=5)
    correct_answer = models.IntegerField(default=0)
