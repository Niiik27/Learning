from django.shortcuts import render



def regView(request):
    return render(request, template_name='reguser/reguser.html')

def loginView(request):
    return render(request, template_name='loginuser/login.html')