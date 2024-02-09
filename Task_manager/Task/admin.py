from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'due_date', 'priority', 'is_complete', 'creation_datetime', 'last_update_datetime')
    list_filter = ('priority',)
    search_fields = ['title']

