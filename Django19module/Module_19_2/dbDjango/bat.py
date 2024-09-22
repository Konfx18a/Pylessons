# Посылаем все команды в shell: python3 manage.py shell < bat.py
from task1.models import Buyer, Game

#Добавляем три игры и трех покупателей
Buyer.objects.create(name='Вася', balance=100.01, age=17)
Buyer.objects.create(name='Петя', balance=10.01, age=31)
Buyer.objects.create(name='Олег', balance=109.11,age=36)
Game.objects.create(title='Doom I', cost=99.11, size=10500, description='Best old game', age_limited=False)
Game.objects.create(title='Leisure Suit Larry', cost=199.11, size=100500,description='Eroric game', age_limited=True)
Game.objects.create(title='Worms', cost=194.11, size=1112500, description='Funny game', age_limited=False)
#Первый по списку взрослый покупатель получает все игры
first_buyer = Buyer.objects.filter(age__gte=18).first()
#Сохраняем его primarykey, чтоб больше ему в будущем не присваивать игры
first_buyer_id = first_buyer.pk
first_buyer.games.set(Game.objects.all())
Buyer.objects.filter(age__gte=18).first().games.set(Game.objects.all())
#Мальцу продаем игры без возрастного лимита
Buyer.objects.filter(age__lt=18).first().games.set(Game.objects.filter(age_limited=False))
# Взрослому пользователю, но не тому кому уже присвоили все игры добавляем все игры кроме одной
Buyer.objects.filter(age__gte=18).exclude(pk=first_buyer_id).first().games.set(Game.objects.all()[1:])
