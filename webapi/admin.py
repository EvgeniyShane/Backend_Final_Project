from django.contrib import admin
from .models import Post, Game, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content')
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Game)
admin.site.register(Comment)