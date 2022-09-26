from django.contrib import admin
from .models import TodoAppModels

@admin.register(TodoAppModels)
class TodoAppModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'created_at']


