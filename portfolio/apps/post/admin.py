from django.contrib import admin

from apps.post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'texto',
        'bio'
    )
