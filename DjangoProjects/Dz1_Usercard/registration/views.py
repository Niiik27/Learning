from django.shortcuts import render
def regView(request):
    return render(request, template_name='./registration/registration.html')