from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# Домашнее задание по теме "Urls и Views. Функциональное и классовое представление."
# ---------------------------------------------------------------------------------
def func_views(request):
    return render(request, 'task2/func_views.html')

class my_views(TemplateView):
    template_name = 'task2/class_views.html'

