from django.db import models

# Question to ask answer only True or False
class Question(models.Model):
    question_text = models.CharField(max_length=200)


# Possible answer True or False, include amount answered
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.BooleanField(default=True)
    correct_answer = models.BooleanField(default=False)
    amount_answer = models.IntegerField(default=0)
