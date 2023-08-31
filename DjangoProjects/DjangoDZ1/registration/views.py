from django.shortcuts import render
def registration_view(request):
    return render(request, template_name='./registration/registration.html')

# Create your views here.
