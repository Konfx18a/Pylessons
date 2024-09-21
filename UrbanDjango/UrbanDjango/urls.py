"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Домашнее задание по теме "Urls и Views. Функциональное и классовое представление."
# ----------------------------------------------------------------------------------
# from task2.views import func_views, my_views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('page2/', my_views.as_view()),
#     path('', func_views),
# ]

# Домашнее задание по теме "Базовые HTML тэги в шаблонах".
# ----------------------------------------------------------------------------------
# from task3.views import main_views, shop_views, basket_views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('platform/', main_views),
#     path('shop/', shop_views),
#     path('basket/', basket_views)
# ]

# Домашнее задание по теме "DTL. Теги, наследование."
# --------------------------------------------------------------------------------

from task4.views import main_views, shop_views, basket_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', main_views),
    path('shop/', shop_views),
    path('basket/', basket_views)
]
