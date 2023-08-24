from django.shortcuts import render

def blogView(request):
    return render(request, template_name='./blog/blog.html')