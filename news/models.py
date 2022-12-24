from django.db import models
from django.urls import reverse_lazy


# Create your models here.


class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Название новости',max_length=150)
    text = models.TextField('Текст новости')
    date_pub = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'