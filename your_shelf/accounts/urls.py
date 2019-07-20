from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('update/<int:pk>/', views.AccountUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.AccountDelete.as_view(), name='delete'),
    path('<str:user_name>/', views.user_detail, name='detail'),
]
