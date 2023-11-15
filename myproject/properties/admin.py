from django.contrib import admin
from .models import Properties
@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('id' ,'agent', 'title', 'slug', 'sale_type', 'property_type','price','is_published')
    list_display_links = ('id','title','is_published','price','agent','slug',)
    search_fields= ('id','title',)
    list_per_page= 25