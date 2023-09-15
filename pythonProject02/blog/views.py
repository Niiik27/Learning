from django.shortcuts import render, get_object_or_404

from .models import Article

app_name = 'blog'
def blogView(request):

    articles = Article.objects.all()
    print(articles)
    return render(request, template_name='./blog/blog.html', context={'articles': articles, 'page_name':'Блог','page_style':'blog'})

def detailView(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'detail/detail.html',{'article_html':article, 'page_name':'Статья','page_style':'detail'})