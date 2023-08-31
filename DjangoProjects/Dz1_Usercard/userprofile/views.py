from django.shortcuts import render
def profileView(request):
    return render(request, template_name='./userprofile/profile.html')