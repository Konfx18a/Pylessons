# Посылаем все команды в shell: python3 manage.py shell < bat.py
# В файле setting добавили базу и обозвали ее test
from task_db.models import Books

#выполняем, что требуется в задании
base = Books.objects.using('test')
# Создать несколько объектов в базе данных
base.create(Title='Алиса в стране чудес', Description='Сказка Льюис Керролл')
base.create(Title='Дневник домового', Description='Сказка Евгений ЧеширКо')
# Используя запросы в базу данных измените один из элементов
book = base.get(Title='Дневник домового').Description="Классика эпистолярного жанра от ЧеширКо"
book.save()
# Выводим все записи
base.all()
# Удаляем с primary key = 3
base.filter(pk=3).delete()
# Выводим с primary key <= 2
base.filter(pk__lte=2)
base.save()




