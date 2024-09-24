from django.core.paginator import Paginator
from django.shortcuts import render

from panagapp.models import Books

NUM_OF_OPTS = [x for x in range(1, 11)]+[20, 30, 40, 50]
def listing(request):
    book_number = request.GET.get("book_numbers", 5)
    books_list = Books.objects.all()
    paginator = Paginator(books_list, book_number)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj, "num_opts": NUM_OF_OPTS, "num": book_number})





