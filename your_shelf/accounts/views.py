from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from .models import CustomUser
from books.models import Book
from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # self.object に save() されたユーザーオブジェクトが格納される
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

def index(request):
    user_list = CustomUser.objects.order_by('username')
    return render(request, 'accounts/account_list.html', {'user_list': user_list})

def user_detail(request, user_name):
    user = CustomUser.objects.get(username=user_name)
    owning_books = Book.objects.filter(owner=user_name)
    borrowing_books = Book.objects.filter(borrower=user_name)
    context = {
        'user': user,
        'owning_books': [owning_book for owning_book in owning_books],
        'borrowing_books': [borrowing_book for borrowing_book in borrowing_books],
    }
    return render(request, 'accounts/account_detail.html', context)
