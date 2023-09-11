from django.shortcuts import render
def mulltabView11(request):
    """
    Этот метод был первым. Потом мне захотелось разбить таблицу на блоки
    :param request:
    :return:
    """
    tab_strs = []
    for i in range(2,10):
        for j in range(2, 10):
            a = i*j
            tab_strs.append(f'{i} x {j} = {a}')
        tab_strs.append("*"*10)
    return render(request, template_name='mulltable/mulltable.html', context={'mull_tab': tab_strs})


def mulltabView(request):
    """
    Теперь итоговый массив рассчитан на обработку внутри двух циклов - внешний меняет основное число
    внутренния - можетели. Это позволит вставить в html всякие символы разбивки, или организовать вывод
    по блокам, а для этого сделать нужные классы
    :param request:
    :return:
    """
    tab_strs = []
    for i in range(1,11):
        var_strs=[]
        for j in range(1, 11):
            a = i*j
            var_strs.append(f'{i} x {j} = {a}')
        tab_strs.append(var_strs)
    return render(request, template_name='mulltable/mulltable.html', context={'mull_tab': tab_strs})