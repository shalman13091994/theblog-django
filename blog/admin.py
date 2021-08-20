from django.contrib import admin
from .models import Post, Category, profile, comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(profile)
admin.site.register(comment)