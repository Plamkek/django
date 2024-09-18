from django.contrib import admin
from .models import Anime, Comment_anime

# Register your models here.
admin.site.register(Anime)
admin.site.register(Comment_anime)
