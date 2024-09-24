from models import Books

books_list = Books.objects.all()
for book in books_list:
    print(book.Title)