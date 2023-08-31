from django.shortcuts import render
def profileView(request):
    foto = request.GET.get('foto')
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    birth = request.GET.get('birth')
    skill_1 = request.GET.get('skill_1')
    skill_2 = request.GET.get('skill_2')
    skill_3 = request.GET.get('skill_3')
    skill_4 = request.GET.get('skill_4')
    skill_5 = request.GET.get('skill_5')
    about = request.GET.get('about')
    context = {
        'foto_html': foto,
        'firstname_html': firstname,
        'lastname_html': lastname,
        'birth_html': birth,
        'skill_1_html': skill_1,
        'skill_2_html': skill_2,
        'skill_3_html': skill_3,
        'skill_4_html': skill_4,
        'skill_5_html': skill_5,
        'about_html': about,
    }
    return render(request, template_name='./userprofile/profile.html',context=context)


# def passwordView(request):
#     newpassword=""
#     length = int(request.GET.get('length'))
#
#     text = []
#     if request.GET.get('lower'):
#         text.extend(list('qwertyuiopasdfghjklzxcvbnm'))
#     if request.GET.get('upper'):
#         text.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
#     if request.GET.get('digits'):
#         text.extend(list('1234567890'))
#     if request.GET.get('symbols'):
#         text.extend(list('_!@%*&'))
#     for i in range(length):
#         # newpassword+=text[random.randint(0,len(text)-1)]
#     return render(request,'password.html',{'new_html_password':newpassword})