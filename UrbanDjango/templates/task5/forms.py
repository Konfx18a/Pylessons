from django import forms


class Sing_up_form(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, label='Введите пароль:')
    password_repeat = forms.CharField(min_length=8, label='Повторите пароль:')
    age = forms.IntegerField(min_value= 5, max_value=100, label='Введите возраст:')


