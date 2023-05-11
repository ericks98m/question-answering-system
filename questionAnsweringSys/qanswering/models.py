from django.db import models

# Create your models here.

class Question(models.Model):
    body_question = models.CharField(max_length=512)
    registration_date   = models.DateTimeField("Registration Date")

    def __str__(self) -> str:
        return self.body_question
  

class Answer(models.Model):
    body_answer = models.CharField(max_length=1024)
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    registration_date   = models.DateTimeField("Registration Date")

    def __str__(self) -> str:
        return self.body_answer
