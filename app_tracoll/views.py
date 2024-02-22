from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from app_tracoll.forms import TranslatedTextForm

from .models import Language, Text, Author , Translation

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

#function based view of home page 
def index(request):

    # objects -> utility provided by Django for several 
    # actions like counting occurences in a database table
    n_texts = Text.objects.all().count()
    n_translations = Translation.objects.all().count()
    n_authors = Author.objects.all().count()
    num_languages = Language.objects.all().count()

    # cookies management
    num_visits = request.session.get('num_visits', 0)
    num_visits = num_visits + 1
    request.session['num_visits'] = num_visits
    request.session.modified = True
    
    # context for index.html template rendering 
    ctx = {
        'num_texts' : n_texts,
        'num_translations' : n_translations,
        'num_authors' : n_authors,
        'num_visits': num_visits,
        'num_languages': num_languages,
    }
    return render(request, 'index.html',context=ctx)

#------------------------------------------------------------------------------------
# views for visualization of a list of authors or translations

class AuthorListView(generic.ListView):
    # pagination parameter
    paginate_by = 8
    # model where to retrieve a list of records
    model = Author

class TranslationListView(generic.ListView):
    # pagination parameter
    paginate_by = 6
    # model where to retrieve a list of records
    model = Translation

    # override of this function
    def get_queryset(self):
        # lookup across relation of Text (calling original_text, name of linked field in 
        # Translation table) and Translation
        # this function will be called and the result will be saved in translation_list object
        # that can be used in template translation_list.html
        final_translations = Translation.objects.filter(original_text__status_of_translation = 'V')
        return final_translations.order_by('translated_title')
 
   
#------------------------------------------------------------------------------------
# views to retrieve details of a single author or translation

class TranslationDetailView(generic.DetailView):
    # model where single instance is retrieved
    model = Translation


class AuthorDetailView(generic.DetailView):
    # model where single instance is retrieved
    model = Author

    # override of this method
    def get_context_data(self, **kwargs):
        # call super class method to mantain same funcionalitites
        ctx = super().get_context_data(**kwargs)

        # add number of final texts of this author to context ONLY when user is NOT logged in
        if(not self.request.user.is_authenticated 
           and not ("can_watch_every_status" in self.request.user.get_all_permissions())
        ):
            #find number of final texts of the given author. ONLY when user is NOT logged in
            number_of_final_texts = Text.objects.filter(author_id=self.get_object().pk).filter(status_of_translation__exact = 'V').count()
            ctx['number_of_final_texts'] = number_of_final_texts

        return ctx
        

@login_required
def translating_page(request, pk):

    # check permission (for Normal user and Administrator)

    if (request.user.has_perm('app_tracoll.permession_of_edit_text_with_every_status')
        or request.user.has_perm('app_tracoll.edit_W_and_E_status_texts')):
        
        text= get_object_or_404(Text, pk=pk)

        #first interaction with form 
        if (request.method != 'POST'):
            
            if(text.status_of_translation == 'W'  or 
               (text.status_of_translation == 'L' and not(request.user.has_perm('app_tracoll.permession_of_edit_text_with_every_status')))):
                previous_data = {
                    # used for texts wating for translation-> return default empty form in this case
                    # or
                    # text under revision by administrator ('L') when user 
                    # has NO editing permission for 'L' texts -> avoid passing translation data
                                'new_translated_title': "",
                                'new_translated_content':  ""
                                }
            else:
                # there are some data already inseted in database and user has permissions-> show data in the form
                    previous_data = {
                            'new_translated_title': text.translation.translated_title,
                            'new_translated_content':  text.translation.translated_content
                            }

            # create form with previous_data
            form = TranslatedTextForm(initial=previous_data)
            # define a context used in page rendering
            ctx = { 'form': form, 'text': text}
            return render(request, "app_tracoll/translating_page.html", ctx)
        else:
            # further interactions with forms
            
            form = TranslatedTextForm(request.POST)
            
            # is_valid() will call every clean method to validate form fields
            if form.is_valid():

                # if text doesn't have a translation, add ONE 
                # as in this branch i'm sure translated 
                # title and translated content (passed with form)
                #  are NOT empty -> thanks to is_valid() 
                if(text.status_of_translation == 'W'):

                    #create new translation object
                    translation_obj = Translation()

                    #link text to translation_obj
                    text.translation = translation_obj
                    text.status_of_translation = 'E'
                    text.save()

                    #link translation_obj to text
                    translation_obj.original_text = text

                    # initialize field of translation_obj
                    translation_obj.creator = request.user
                    translation_obj.translated_title = form.cleaned_data['new_translated_title']
                    translation_obj.translated_content = form.cleaned_data['new_translated_content']

                    # save translation
                    translation_obj.save()

                    # link translation to user
                    request.user.translation_set.add(translation_obj)
                    request.user.save()

                else:
                    # translation is already present -> show title and text of translation in the form
                    text.translation.translated_title = form.cleaned_data['new_translated_title']
                    text.translation.translated_content = form.cleaned_data['new_translated_content']
                    text.translation.save()
                
                # after correct data insertion in form, user will be
                # redirected to author's detail page
                return HttpResponseRedirect(reverse("author-detail", args=[text.author.pk]))

            else:
                # had some form validation error, return form 
                ctx = { 'form': form, 'text': text }
                # redirect to form page, Django's automatic facilities
                # will attach error messages to interested fields
                return render(request, 'app_tracoll/translating_page.html', ctx)
    else:
        # will automatically redirect to 403.html page
        raise PermissionDenied()

