from django.db import models


class Article(models.Model):
    title = models.CharField('Заголовок',max_length=15)  # Ограниченная строка
    desc= models.TextField('Описание')  # Ограниченная строка
    image= models.ImageField('Изображение',upload_to='blog/image')  # строка по изображению (отдельный тип данных)
    date = models.DateField('Дата')  # Дата
    url = models.URLField('Доп. источник',blank=True)  # Ссылка
    def __str__(self):
        return f"{self.title} | {self.date}"
    class Meta:
        verbose_name = 'readable'
        verbose_name_plural = 'Статьи'

