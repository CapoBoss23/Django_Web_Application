from django.contrib import admin

# Register your models here.

from .models import Text, Author, Translation, Language

#------------------------------------------------------------------------------------------
#admin page customization 


class AuthorAdmin(admin.ModelAdmin):
    # visualization in list of authors in admin page
    list_display = ('name_of_author', 'type_of_author')


class TextAdmin(admin.ModelAdmin):
    # visualization in list of texts in admin page
    list_display = ('title','author','type_of_text','original_language')


class TranslationAdmin(admin.ModelAdmin): 
    # visualization in list of translations in admin page
    list_display = ('translated_title', 'original_text','creator')


#------------------------------------------------------------------------------------------
#register model's entities to make them visible in admin page
admin.site.register(Text, TextAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Translation, TranslationAdmin)
admin.site.register(Language)
