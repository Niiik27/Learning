from django.shortcuts import render
import datetime
from utils import get_num_in_russian, russian_month
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
    left_days_str = get_num_in_russian(left_days,["день","дня","дней"])
    left_hours = int((total_seconds % 86400)/3600)
    left_hours_str = get_num_in_russian(left_hours, ["час","часа","часов"])
    left_minutes = int((total_seconds % 3600 )/60)
    left_minutes_str = get_num_in_russian(left_minutes, ["минута","минуты","минут"])
    left_seconds = int(total_seconds - left_days*86400 - left_hours*3600 - left_minutes*60)
    left_seconds_str = get_num_in_russian(left_seconds, ["секунда", "секунды", "секунд"])
    """
    Если измерять в секeундах, то можно пропустить день программиста. По этому нужно уменьшить точность
    Измеряем в днях
    """
    coder_txt = f'День программиста: {prog_day.day} {russian_month[prog_day.month]} {prog_day.year} года'
    if left_days>0:
        left_time = f"До дня программиста {'остался' if left_days%10==1 else 'осталось'}: {left_days_str} {left_hours_str} {left_minutes_str} {left_seconds_str}"
    elif left_days<0:
        left_time = f'Со дня программиста проошло: {left_days_str} {left_hours_str} {left_minutes_str} {left_seconds_str} секунд'
    else:
        if left_seconds >= 0:
            left_time = f'До дня программиста осталось совсем немного: {left_hours_str} {left_minutes_str} {left_seconds_str}'
        else:
            left_time = f'Сегодня день программиста! Он идет уже: {left_hours_str} часов {left_minutes_str} минут {left_seconds_str}'

    return render(request, template_name='coderday/coderday.html', context={'coder_txt': coder_txt,'left_txt': left_time})
