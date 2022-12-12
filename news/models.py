from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField('Название новости',max_length=150)
    text = models.TextField('Текст новости')
    date_pub = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'