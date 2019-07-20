from django.urls import path
from . import views
from .views import BookCreate, BookUpdate, BookDelete
app_name='books'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', BookCreate.as_view(), name='create'),
    path('<str:book_title>/',  views.book_detail, name='detail'),
    path('<str:pk>/update/', BookUpdate.as_view(), name='update'),
    path('<str:pk>/delete/', BookDelete.as_view(), name='delete'),
]
