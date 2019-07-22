from django.shortcuts import render
from accounts.models import CustomUser
from books.models import Book
# Create your views here.
def profile_detail(request, pk):
    user = CustomUser.objects.get(username=pk)
    owning_books = Book.objects.filter(owner=user)
    borrowing_books = Book.objects.filter(borrower=user)
    context = {
        'user': user,
        'owning_books': [owning_book for owning_book in owning_books],
        'borrowing_books': [borrowing_book for borrowing_book in borrowing_books],
    }
    return render(request, 'profiles/profile_detail.html', context)
