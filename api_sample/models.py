from django.db import models

# Create your models here.

class Sample(models.Model):
    title = models.CharField(max_length=50, verbose_name='タイトル')
    contributor = models.CharField(max_length=50, verbose_name='投稿者')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')

    def __str__(self):
        return self.title