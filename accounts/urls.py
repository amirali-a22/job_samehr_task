from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register', views.user_register, name='user_register'),
]
