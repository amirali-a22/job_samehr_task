from django.contrib import admin

from simple_history import register
from django.contrib.auth.models import User
from .models import Category

admin.site.register(Category)
register(User)
register(Category)
