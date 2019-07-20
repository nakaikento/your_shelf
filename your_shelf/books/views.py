from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from users.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .forms import BookForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book
from django.contrib import messages
# BookDetail
from django.views.generic import DetailView

def index(request):
    book_list = Book.objects.order_by('-publish_date')[:5]
    return render(request, 'books/book_list.html', {'book_list':book_list})

# class BookDetail(DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

class BookCreate(CreateView):
    model = Book
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('books:index')

    fields = ['attrs', 'owner', 'borrower', 'title', 'isbn', 'image',\
     'author', 'price', 'publisher', 'publish_date', 'description']

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」Created!'.format(form.instance))
        return result

class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('books:index')
    fields = ['attrs', 'owner', 'borrower', 'title', 'isbn', 'image',\
     'author', 'price', 'publisher', 'publish_date', 'description']
    tempalte_name_suffix = '_update_form'


class BookDelete(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:index')


def book_detail(request, book_title):
    book = Book.objects.get(title=book_title)
    if request.method == 'POST':
        #貸し出しリクエストに必要な変数
        owner_name = book.owner
        borrower_name = "今ログインしている人"
        owner_email = User.objects.get(name= owner_name).email

        subject = "メール貸出リクエスト"
        message = "こんにちは！\n\n{0}さんが{1}さんの【{2}】を貸してほしいそうです。"\
        .format(borrower_name,owner_name,book)
        from_email = "loginner_email@gmail.com"
        recipient_list = [
            owner_email
        ]
        send_mail(subject, message, from_email, recipient_list,)
    return render(request, 'books/book_detail.html', {'book':book})
