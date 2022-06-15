from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)  # 자동 현재 시간
    end_date = models.DateTimeField(null=True, blank=True)  # 블랭크도 추가해야 값이 없어도 됨.

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo


class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)