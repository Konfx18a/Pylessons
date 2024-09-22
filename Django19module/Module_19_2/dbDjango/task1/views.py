from django.shortcuts import render
from .models import *
# Create your views here.
from templates.forms import Sing_up_form

# Create your views here.
errors = {'not_same_pswd': 'Пароли не совпадают', 'young_age': 'Вы должны быть старше 18!',
          'user_exist': 'Пользователь уже существует'}
users_db = ['Петя', 'Вася', 'Коля', 'Таня']

def check_input(username,pswd,pswd_repeat,age):
    if pswd != pswd_repeat:
        answ = errors['not_same_pswd']
    else:
        if check_user(username):
            answ = f'Пользователь, {username} уже существует!'
        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            answ = f'Приветствуем, {username} !'
    return answ

def check_user(username):
    buyers = Buyer.objects.all()
    for buyer in buyers:
        print(buyer.name)
        if buyer.name == username:
            return True
    return False

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
    else:
        form = Sing_up_form()
    context['form'] = form
    return render(request, 'platform.html', context)

from templates.texts import strings as st


# Create your views here.

def main_views(request):
    context = st.main_page
    return render(request, 'platform.html', context)


def shop_views(request):
    games = Game.objects.all()
    context ={
      'games': games,
        'button': "Купить",
        'button_back': "Вернуться обратно",
    }
    return render(request, 'games.html', context)


def basket_views(request):
    context = st.basket
    return render(request, 'card.html', context)