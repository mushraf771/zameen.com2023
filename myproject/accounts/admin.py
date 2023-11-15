from django.contrib import admin
from .models import UserAccount
@admin.register(UserAccount)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'is_active', 'is_agent', 'is_staff')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'id')
    list_per_page = 20
