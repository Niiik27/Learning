from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User# подключение Базы данных по умолчанию
from django.contrib.auth import login
from django.db import IntegrityError
app_name = 'reguser'

def reguserView(request):
    if request.method == "GET":
        return render(request, 'reguser/reguser.html', {'formuser':UserCreationForm(), 'page_name':'Регистрация'})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm(),'error':'Такой логин уже занят', 'page_name':'Регистрация - выберите другой логин'})
        else:
            return render(request, 'reguser/reguser.html', {'formuser': UserCreationForm(),'error':'Пароли не совпадают', 'page_name':'Введите совпадающие пароли',})




def loginuserView(request):
    return render(request, 'loginuser/login.html',{'page_name':'Вход','page_style':'loguser'})