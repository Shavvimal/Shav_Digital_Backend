from django.contrib import admin
from .models import ContactPost

class ContactPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_created')
    list_filter = ('email', "name")
    list_display_links = ('id', 'name')
    search_fields = ['name', 'content']
    list_per_page = 25

admin.site.register(ContactPost, ContactPostAdmin)