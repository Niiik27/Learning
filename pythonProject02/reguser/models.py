from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    firstname = models.CharField('Имя',max_length=20)
    secondname = models.CharField('Фамилия',max_length=20)
    age = models.IntegerField('Возраст')
    about = models.TextField('О себе', blank=True)
    image_profile = models.ImageField('Аватарка', upload_to='profile/image/')
    # Внешний ключ
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} | {self.secondname} | {self.age}"
    class Meta:
        verbose_name = 'Пользователя++'
        verbose_name_plural = 'Информация о пользователе'

def create_user_profile(sender,instance, created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()