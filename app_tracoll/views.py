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
    model = Translation

    #override of this function
    def get_queryset(self):
        #lookup across relation of Text (calling original_text, name of linked field in 
        # Translation table) and Translation
        # this function will be called and the result will be saved in translation_list object
        # that can be used in template translation_list.html
        final_translations = Translation.objects.filter(original_text__status_of_translation = 'V')
        return final_translations.order_by('translated_title')

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

from django.shortcuts import get_object_or_404

class AuthorDetailView(generic.DetailView):
    #login_url = '/accounts/login/' 
    model = Author


    ## disttinguo su base di permesso qui dentro e faccio cosa mi serve  -> ASK PROF COME GET OGGETTO SINGOLO AUTORE??
    ## FORSE CHECK PERMESSO DENTRO CONTEXT DATA COULD BE OK, OCCHIO
    #def get_context_data(self, **kwargs):
    #    if (self.request.user.is_authenticated 
    #        and (self.request.user.has_perm('app_tracoll.can_watch_every_status'))
    #        ):# if normal user or admin -> no need to filter data ,IT WORKS AS USUAL

    #            context = super(AuthorDetailView, self).get_context_data(**kwargs)
    #            #------------------------DEBUGGING----------------------------
    #            print("DEBUG:")
    #            print(context)
    #            #print(type(context))
    #            #-------------------------------------------------------------
    #            #return super(AuthorDetailView, self).get_context_data(**kwargs)
    #            return context
            
    #    else: # if NOT authenticated user -> return ONLY 'V' texts
    #            context = super(AuthorDetailView, self).get_context_data(**kwargs)

    #            final_texts = Author.text_set.filter(status_of_translation_contains = 'V')
    #            final_texts_of_this_author = final_texts.objects.filter(author__name_of_author = self.object.pk)

    #            #add list to context
    #            context['final_texts'] = final_texts_of_this_author
    #            #get specific author object
    #            #context['author'] = Author.objects.filter(pk = self.object.pk)

    #            ###------------------------DEBUGGING----------------------------
    #            ##print("DEBUG:")
    #            ##print(context)
    #            ##print("DEBUG:")
    #            ##print(type(context['author']))
    #            ###-------------------------------------------------------------

    #            ###get filtered (ONLY 'V') texts to display in template
    #            ##for text in context['author'].text_set:
    #            ##    if(text.status_of_translation != 'V'):
    #            ##        context['author'].text_set.remove(text)
    #            ##context['author'].text_set = context['author'].text_set.objects.filter(status_of_translation__exact == 'V')
    #            ##Restaurant.objects.filter(r_courses__course =self.object, rating__gt=4)

    #            return context

        



    #author = get_object_or_404(Author, pk)

    #if(perms)
        # uetnte normale
    #else
        #uetnte admin

    #def get_queryset(self):
    #    final_translations_set = self.text_set.all.objects.filter(status_of_translation__exact = 'V')
    #    final_translations_count = final_translations_set.count()
    #    return (final_translations_count != 0)
