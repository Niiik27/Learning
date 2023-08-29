from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=15)  # Ограниченная строка
    desc= models.CharField(max_length=50)  # Ограниченная строка
    image= models.ImageField(upload_to='blog/image')  # строка по изображению (отдельный тип данных)
    date = models.DateField()  # Дата
    url = models.URLField()  # Ссылка
