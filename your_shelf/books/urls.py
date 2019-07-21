from django.urls import path
from . import views
app_name='books'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.BookCreate.as_view(), name='create'),
    path('<str:pk>/',  views.book_detail, name='detail'),
    path('<str:pk>/update/', views.BookUpdate.as_view(), name='update'),
    path('<str:pk>/delete/', views.BookDelete.as_view(), name='delete'),
]
