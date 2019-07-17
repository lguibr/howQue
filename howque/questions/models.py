from django.db import models

# Create your models here.

class Question(models.Model):
    path_question = models.CharField(max_length=200, unique=True)
    path_answer = models.CharField(max_length=200, unique=True)
    tags = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    

