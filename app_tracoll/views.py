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

    #cookies management
    num_visits = request.session.get('num_visits', 0)
    num_visits = num_visits + 1
    request.session['num_visits'] = num_visits
    request.session.modified = True
    
    ctx = {
        'num_texts' : n_texts,
        'num_translations' : n_translations,
        'num_authors' : n_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html',context=ctx)

#for visualization of Author, Translations, Texts in other pages
class AuthorListView(generic.ListView):
    #login_url = '/accounts/login/'
    paginate_by = 3
    model = Author

class TranslationListView(generic.ListView):
    paginate_by = 3
    model = Translation    #override of this function    def get_queryset(self):        #lookup across relation of Text (calling ) and Translation        # this function will be called and the result will be saved in translation_list object        # that can be used in template translation_list.html        final_translations = Translation.objects.filter(original_text__status_of_translation = 'V')        return final_translations.order_by('translated_title')

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


