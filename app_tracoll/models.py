from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):

    AUTHOR_TYPOLOGY=(('P', 'Poet'),('S','Songwriter'),('B','Band'),)
    type_of_author = models.CharField(max_length = 1,choices = AUTHOR_TYPOLOGY,
                              blank = False, help_text = 'Typology of author')
    name_of_author = models.CharField(max_length = 100) 

    class Meta:
        ordering = ['name_of_author']
        permissions = (("can_watch_every_status", "You can watch every text status"),)

    def __str__(self):
        return f'{self.name_of_author}' 

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])




class Text(models.Model):

    TEXT_TYPOLOGY = (('P', 'Poem'),('S', 'Song'),)
    type_of_text= models.CharField(max_length = 1,choices = TEXT_TYPOLOGY,
                                   blank = False,help_text = 'Type of text')
    
    # title and content CANNOT be blank
    title = models.CharField(max_length= 100, blank= False)
    content = models.TextField(max_length= 2000, blank= False)

    POSSIBLE_LANGUAGES = (('E', 'English'),('F', 'French'),('S', 'Spanish'),)
    original_language = models.CharField(max_length = 1,choices = POSSIBLE_LANGUAGES,
                                         blank = False,help_text = 'language of the original text')
    
    # null = True --> author can be unknown
    author= models.ForeignKey(Author, null = True, on_delete= models.SET_NULL)

    #choices for translation state
    TRANSLATION_STATE=(('W','Waiting for translation'),
                       ('L','Under revision by administrator'),
                       ('E','Existing translation and editable by authenticated users'),
                       ('V','Final translation NOT editable anymore'),)
    status_of_translation = models.CharField(max_length = 1,choices = TRANSLATION_STATE,
                              blank = False, default = 'W',
                              help_text = 'State of traslation')

    class Meta:
        ordering = ['title']
        # permissions = (("can_mark_returned", "Set book as returned"),)
   
    #method called when in admin page to visualize data instance
    def __str__(self):
        return f'{self.id}, {self.title} , {self.author}'

from django.contrib.auth.models import User


class Translation(models.Model):
    
    translated_title = models.CharField(max_length=100)   
    translated_content = models.TextField(max_length=2000)
    original_text =models.OneToOneField(Text, null= True,  on_delete = models.SET_NULL) #null= true? on_delete = models.SET_NULL?

    creator =models.ForeignKey(User,on_delete = models.SET_NULL,
                                 null = True,blank = True)

    class Meta:
        ordering = ['translated_title']
        permissions = (("permession_of_edit_text_with_every_status", "You can edit every text in every status"),
        ("edit_W_and_E_status_texts","You can edit W and E text status"))

    def __str__(self):
        return f'{self.translated_title}'

    #used in reverse function
    def get_absolute_url(self):
        return reverse('translation-detail', args=[str(self.id)])