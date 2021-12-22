from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'category', 'chapter', 'sub_chapter', 'title', 'date_created')
    list_filter = ('category', "chapter")
    list_display_links = ('id', 'title')
    search_fields = ['title', 'content']
    list_per_page = 25
    summernote_fields = ('content', )

admin.site.register(BlogPost, BlogPostAdmin)
