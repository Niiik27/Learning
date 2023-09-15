from django.shortcuts import render

def homeView(request):

    return render(request, './home/home.html', {'page_name': 'Домашняя страница','page_style':'home'})




# Create your views here.
