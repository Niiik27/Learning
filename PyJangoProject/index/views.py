import random

from django.shortcuts import render


def indexView(request):
    return render(request, 'index.html')

def passwordView(request):
    newpassword=""
    length = int(request.GET.get('length'))

    text = []
    if request.GET.get('lower'):
        text.extend(list('qwertyuiopasdfghjklzxcvbnm'))
    if request.GET.get('upper'):
        text.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('digits'):
        text.extend(list('1234567890'))
    if request.GET.get('symbols'):
        text.extend(list('_!@%*&'))
    for i in range(length):
        newpassword+=text[random.randint(0,len(text)-1)]
    return render(request,'password.html',{'new_html_password':newpassword})


