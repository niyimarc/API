from django.contrib import admin
from .models import BlogPost, PostCategory

# Register your models here.

admin.site.register((BlogPost, PostCategory))
