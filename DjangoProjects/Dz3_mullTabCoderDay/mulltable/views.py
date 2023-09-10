from django.shortcuts import render
def mulltabView11(request):
    tab_strs = []
    for i in range(2,10):
        for j in range(2, 10):
            a = i*j
            tab_strs.append(f'{i} x {j} = {a}')
        tab_strs.append("*"*10)
    return render(request, template_name='mulltable/mulltable.html', context={'mull_tab': tab_strs})


def mulltabView(request):
    tab_strs = []
    for i in range(2,10):
        var_strs=[]
        for j in range(2, 10):
            a = i*j
            var_strs.append(f'{i} x {j} = {a}')
        tab_strs.append(var_strs)
    return render(request, template_name='mulltable/mulltable.html', context={'mull_tab': tab_strs})