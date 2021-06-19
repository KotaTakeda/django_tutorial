from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # 人間可読なfield名を指定

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Questionとのリレーションシップを定義
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)