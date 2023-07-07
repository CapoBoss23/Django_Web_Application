from django.contrib import admin

# Register your models here.

from .models import Text, Author, Translation

admin.site.register(Text)
admin.site.register(Author)
admin.site.register(Translation)
