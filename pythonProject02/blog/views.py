from django.shortcuts import render, get_object_or_404

from .models import Article

app_name = 'blog'
def blogView(request):
    articles = Article.objects.all()
    return render(request, template_name='./blog/blog.html', context={'articles': articles})

def detailView(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'detail/detail.html',{'article_html':article})