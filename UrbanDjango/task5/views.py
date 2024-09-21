from django.shortcuts import render
from django.shortcuts import HttpResponse

from templates.task5.forms import Sing_up_form

# Create your views here.
errors = {'not_same_pswd': 'Пароли не совпадают', 'young_age': 'Вы должны быть старше 18!',
          'user_exist': 'Пользователь уже существует'}
users_db = ['Петя', 'Вася', 'Коля', 'Таня']

def check_input(username,pswd,pswd_repeat,age):
    if age < 18:
        answ = errors['young_age']
    elif pswd != pswd_repeat:
        answ = errors['not_same_pswd']
    elif username in users_db:
        answ = errors['user_exist']
    else:
        answ = f'Приветствуем, {username} !'
    return answ

def sign_up_by_html(request):
    context={}
    if request.method == "POST":
        username = request.POST.get("username")
        pswd = request.POST.get("password")
        pswd_repeat = request.POST.get('password_repeat')
        age = request.POST.get('age')
        context['info'] = check_input(username, pswd, pswd_repeat, age)
        # return HttpResponse(check_input(username, pswd, pswd_repeat, age))

    return render(request, 'task5/registration_page.html', context)


def sign_up_by_django(request):
    context={}
    if request.method == "POST":
        form = Sing_up_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pswd = form.cleaned_data['password']
            pswd_repeat = form.cleaned_data['password_repeat']
            age = form.cleaned_data['age']
            context['info'] = check_input(username, pswd, pswd_repeat, age)
        else:
            context['info'] = 'Возраст должен быть от 5 до 100!!'

        # return HttpResponse(check_input(username, pswd, pswd_repeat, age))

    else:
        form = Sing_up_form()
    context['form'] = form
    return render(request, 'task5/registration_page.html', context)