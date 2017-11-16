from django.db import models

# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length = 140)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice (models.Model):
    answer_text = models.CharField(max_length = 20)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

class Choice2 (models.Model):
    answer_text = models.CharField(max_length = 20)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text