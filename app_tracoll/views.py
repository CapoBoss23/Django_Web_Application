from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Text, Author , Translation

from django.contrib.auth.mixins import LoginRequiredMixin


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

#for visualization of Author, Translations, Texts in other pages
class AuthorListView(generic.ListView):
    #login_url = '/accounts/login/'
    paginate_by = 3
    model = Author

class TranslationListView(generic.ListView):
    paginate_by = 3
    model = Translation

#class TextListView(LoginRequiredMixin, generic.ListView):
#    #fallback page if user is NOT logged in
#    login_url = '/accounts/login/'
#    paginate_by = 3
#    model = Text
    

# views used to see details of a single text and translation or author

# LoginRequiredMixin,
class TranslationDetailView(generic.DetailView):
    #login_url = '/accounts/login/' 
    model = Translation

class AuthorDetailView(generic.DetailView):
    #login_url = '/accounts/login/' 
    model = Author


