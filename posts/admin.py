from django.contrib import admin
from .models import Post, Comment
# Register your models here.

#admin.site.register(Post)

@admin.register(Post) #Decorator -> Auto generación de código
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'created_date')