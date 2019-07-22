from django.urls import path
from . import views
app_name='profiles'
urlpatterns = [
    path('<str:pk>', views.profile_detail, name='detail'),
    ]
