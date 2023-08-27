from django.urls import path
from . import views




urlpatterns = [
    path('', views.main, name='main'),
    path('leave_message/', views.leave_message, name='leave_message'),
    path('login/', views.user_login, name='login'),
    path('photos/', views.photos, name='photos'),


]