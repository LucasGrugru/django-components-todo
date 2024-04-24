from django.contrib import admin

from apps.todo.models import Todo, TodoItem


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'done')
    list_filter = ('title', 'done')
    search_fields = ('title', 'description')


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done')
    list_filter = ('title', 'done')
    search_fields = ('title', )
