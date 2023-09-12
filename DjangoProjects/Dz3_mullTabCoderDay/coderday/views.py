from django.shortcuts import render
import datetime

def timedelta_to_dhms(duration):
    # преобразование в дни, часы, минуты и секунды
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds
def coderdayView(request):
    today = datetime.date.today()
    first_day_year = datetime.datetime(today.year, 1, 1,0,0,0)
    delta = datetime.timedelta(days=256)
    prog_day = first_day_year + delta
    # days, hours, minutes, seconds = timedelta_to_dhms(delta)
    deltaNow = datetime.datetime(prog_day.year, prog_day.month, prog_day.day,prog_day.hour,prog_day.minute,prog_day.second) - datetime.datetime.now()
    total_seconds = deltaNow.total_seconds()
    left_days = int(total_seconds / 86400)
    left_hours = int((total_seconds % 86400)/3600)
    left_minutes = int((total_seconds % 3600 )/60)
    left_seconds = int(total_seconds - left_days*86400 - left_hours*3600 - left_minutes*60)
    """
    Если измерять в секeундах, то можно пропустить день программиста. По этому нужно уменьшить точность
    Измеряем в днях
    """
    coder_txt = f'День программиста: {prog_day.day}.{prog_day.month}.{prog_day.year}'
    if left_days>0:
        left_time = f'До дня программиста осталось: {left_days} дней {left_hours} часов {left_minutes} минут {left_seconds} секунд'
    elif left_days<0:
        left_time = f'Со дня программиста проошло: {-left_days} дней {left_hours} часов {-left_minutes} минут {-left_seconds} секунд'
    else:
        if left_seconds >= 0:
            left_time = f'До дня программиста осталось совсем немного: {left_hours} часов {left_minutes} минут {left_seconds} секунд'
        else:
            left_time = f'Сегодня день программиста! Он идет уже: {-left_hours} часов {-left_minutes} минут {-left_seconds} секунд'

    return render(request, template_name='coderday/coderday.html', context={'coder_txt': coder_txt,'left_txt': left_time})
