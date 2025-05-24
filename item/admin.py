from django.contrib import admin

# Register your models here.
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

