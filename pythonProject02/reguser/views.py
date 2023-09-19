from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User# подключение Базы данных по умолчанию
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'loginuser/login.html', {'formuser': form, 'page_name': 'Вход'})
    else:
        form = AuthenticationForm(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        
    if user is not None:
        try:
            login(request,user)
            return redirect('home')
        except ValueError:
            return render(request, 'loginuser/login.html', {'formuser': form,'error':'Неверный логин или пароль1', 'page_name': 'Вход'})
        except AttributeError:#Альтернатива else
            return render(request, 'loginuser/login.html', {'formuser': form,'error':'Неверный логин или пароль2', 'page_name': 'Вход'})
    else:
        return render(request, 'loginuser/login.html', {'formuser': form,'error':'Неверный логин или пароль3', 'page_name': 'Вход'})
        

    
def logoutuserView(request):
    logout(request)
    return redirect('home')



def profileView(request):
    user_profile = request.user.userprofile
    return render(request,'profile/profile.html',{'user_profile':user_profile})
def profileupView(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance = user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Профиль успешно обновлен')
            return redirect('profile')
    else:
        form = UserProfileForm(instance = user_profile)
        return render(request,'profile/profileup.html',{'form':form})