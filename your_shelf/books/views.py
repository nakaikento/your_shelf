from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .forms import BookForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book
from django.contrib import messages
# BookDetail
from django.views.generic import DetailView

def index(request):
    # book_list = Book.objects.order_by('-publish_date')
    data_science = Book.objects.filter(attrs='Data Science')
    web = Book.objects.filter(attrs='Web')
    mobile = Book.objects.filter(attrs='Mobile')
    cloud = Book.objects.filter(attrs='Cloud')
    entre = Book.objects.filter(attrs='起業')
    etc = Book.objects.filter(attrs='その他')
    data_science = [book for book in data_science]
    web = [book for book in web]
    mobile = [book for book in mobile]
    entre = [book for book in entre]
    etc = [book for book in etc]
    context = {
        'genre_list' : [data_science, web, mobile, cloud, entre, etc]
    }
    # return render(request, 'books/book_list.html', {'book_list':book_list})
    return render(request, 'books/book_list.html', context)

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


def book_detail(request, pk):
    book = Book.objects.get(title=pk)
    if request.method == 'POST':
        #貸し出しリクエストに必要な変数
        owner_name = book.owner
        # 現在ログインしている人の名を取る
        borrower_name = request.user
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
