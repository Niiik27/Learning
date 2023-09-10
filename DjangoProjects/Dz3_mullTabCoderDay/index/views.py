import datetime
import locale
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)

from django.shortcuts import render

# Create your views here.
def indexView(request):
    time_now = datetime.datetime.now().time().strftime('Сейчас %H часов %M минут')
    today_date = datetime.datetime.now().date().strftime('%d %B %Y года')

    return render(request, template_name='index/index.html',context={'today_html_var':today_date,'now_html_var':time_now,})