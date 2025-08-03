from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'completed', 'priority', 'due_date', 'created_at')
    list_filter = ('completed', 'priority', 'due_date', 'category')
    search_fields = ('title', 'description', 'owner__email')
    autocomplete_fields = ('owner', 'category', 'shared_with')
    filter_horizontal = ('shared_with',)
