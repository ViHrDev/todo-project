from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ToDo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Name Tasks', max_length=500)
    is_complete = models.BooleanField('Completed', default=False)
    desc = models.CharField('description',max_length=500)
    date = models.DateTimeField('Date and time creation',auto_now_add=True)
    date_end = models.DateTimeField('Date and time closed', auto_now=True)

    class Meta:
        verbose_name = 'quest'
        verbose_name_plural = 'questions'

    def __str__(self):
        return self.title
