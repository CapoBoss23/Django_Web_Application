from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Text, Author , Translation

def index(request):
    # objects -> utility class provided by Django for several 
    # actions like counting occurences of a certain type
    n_texts = Text.objects.all().count()
    n_translations = Translation.objects.all().count()
    n_authors = Author.objects.all().count()
    
    ctx = {
        'num_texts' : n_texts,
        'num_translations' : n_translations,
        'num_authors' : n_authors,
    }
    return render(request, 'index.html',context=ctx)

#for visualization of Author and Translations in 2 other pages
class AuthorListView(generic.ListView):
	model = Author

class TranslationListView(generic.ListView):
	model = Translation
