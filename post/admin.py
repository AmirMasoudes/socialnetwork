from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'update_date')
    search_fields = ('slug', 'user')
    list_filter = ('update_date',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)
