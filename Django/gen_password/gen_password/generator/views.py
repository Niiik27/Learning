from django.shortcuts import render

# Create your views here.
def home(request):
    print(request)
    return 101