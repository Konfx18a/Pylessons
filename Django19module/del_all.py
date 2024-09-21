# Для очистки таблиц, ну и когда проверял работу bat.py
from task1.models import Buyer, Game
Buyer.objects.all().delete()
Game.objects.all().delete()
