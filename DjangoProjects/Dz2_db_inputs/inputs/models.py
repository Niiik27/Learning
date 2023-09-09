from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=15)  # Ограниченная строка
    desc= models.CharField(max_length=50)  # Ограниченная строка
    image= models.ImageField(upload_to='blog/image')  # строка по изображению (отдельный тип данных)
    date = models.DateField()  # Дата
    url = models.URLField()  # Ссылка
    number = models.PositiveSmallIntegerField()
    JASONvalue = models.JSONField()
    booleaValue = models.BooleanField()
    timeValue = models.TimeField()
    dateTimeValue = models.DateTimeField()
    # decimalValue = models.DecimalField()
    durationValue = models.DurationField()
    floatValue = models.FloatField()
    emailValue = models.EmailField()
    ipValue = models.GenericIPAddressField()
    # comaValue = models.CommaSeparatedIntegerField()
    # nullBooleanValue = models.NullBooleanField()


    # fileValue = models.FilePathField()
    uuidValue = models.UUIDField()
    slugValue = models.SlugField()
    # # oneTwoOneField = models.OneToOneField()
    binaryValue = models.BinaryField()
    bifPosIntField = models.PositiveBigIntegerField()