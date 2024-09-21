from django.shortcuts import render
from templates.task3.texts import strings as st
# Create your views here.


def main_views(request):
    context = st.main_page
    return render(request, 'task3/platform.html', context)


def shop_views(request):
    context = st.shop
    return render(request, 'task3/games.html', context)


def basket_views(request):
    context = st.basket
    return render(request, 'task3/card.html', context)