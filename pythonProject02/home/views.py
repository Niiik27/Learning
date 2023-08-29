from django.shortcuts import render

def homeView(request):

    return render(request, template_name='./home/home.html')




# Create your views here.
