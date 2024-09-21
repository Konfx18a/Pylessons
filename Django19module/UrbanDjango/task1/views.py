from django.shortcuts import render

# Create your views here.
from task1.templates.task1.forms import Sing_up_form
from task1.templates.task1.texts import strings as st

def main_views(request):
    context = st.main_page
    return render(request, 'task1/platform.html', context)


def shop_views(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    context ={
      'games': games,
        'button': "Купить",
        'button_back': "Вернуться обратно",
    }
    return render(request, 'task1/games.html', context)


def basket_views(request):
    context = st.basket
    return render(request, 'task1/card.html', context)

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

def sign_up_by_django(request):
    context = {}
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
    return render(request, 'task1/registration_page.html', context)