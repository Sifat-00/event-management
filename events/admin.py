# from django.contrib import admin

# # Register your models here.
from django.contrib import admin
from .models import Category
from .models import Category, Event


admin.site.register(Category)

admin.site.register(Event)
