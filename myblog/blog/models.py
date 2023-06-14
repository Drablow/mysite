from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    """ Данные о посте """
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    date_posted = models.DateTimeField('date', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
