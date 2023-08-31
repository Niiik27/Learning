from django.shortcuts import render
def userprofile_view(request):
    return render(request, template_name='./userprofile/userprofile.html')

# Create your views here.
