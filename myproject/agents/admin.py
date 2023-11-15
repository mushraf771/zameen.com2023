from django.contrib import admin
from .models import Agent


@admin.register(Agent)
class AgentRegister(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone',
                    'top_seller', 'date_hired',)
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'id')
    list_per_page = 20
