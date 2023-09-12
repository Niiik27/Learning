import datetime
from utils import get_num_in_russian, russian_month
from django.shortcuts import render

def indexView(request):

    hour = get_num_in_russian(datetime.datetime.now().time().hour,["час","часа","часов"])
    minute = get_num_in_russian(datetime.datetime.now().time().minute,["минута","минуты","минут"])
    time_now = f'Сейчас {hour}, {minute}'


    day = datetime.datetime.now().day
    month = russian_month[datetime.datetime.now().month]
    year = datetime.datetime.now().year
    current_date = f"{day} {month} {year}"
    today_date = f"Сегодня {current_date} года"
    return render(request, template_name='index/index.html',context={'today_html_var':today_date,'now_html_var':time_now,})