from django.contrib import admin
from . models import TodoItem



class TodoItemAdimn(admin.ModelAdmin):
    pass

admin.site.register(TodoItem, TodoItemAdimn)


