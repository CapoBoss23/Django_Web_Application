from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):

    AUTHOR_TYPOLOGY=(('P', 'Poet'),('S','Songwriter'),('B','Band'),)
    type_of_author = models.CharField(max_length = 1,choices = AUTHOR_TYPOLOGY,
                              blank = False, help_text = 'Typology of author')
    name_of_author = models.CharField(max_length = 100, blank = False) 

    class Meta:
        ordering = ['name_of_author']
        permissions = (("can_watch_every_status", "You can watch every text status"),)
    
    # used for visualization in admin page
    def __str__(self):
        return f'{self.name_of_author}' 

    # used in Author List to get URL to specific author
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Language(models.Model):

    name_of_language = models.CharField(max_length= 100, blank= False)

    class Meta:
        ordering = ['name_of_language']
   
    # used for visualization in admin page
    def __str__(self):
        return f'{self.name_of_language}'


class Text(models.Model):

    TEXT_TYPOLOGY = (('P', 'Poem'),('S', 'Song'),)
    type_of_text= models.CharField(max_length = 1,choices = TEXT_TYPOLOGY,
                                   blank = False,help_text = 'Type of text')
    
    # title and content CANNOT be blank
    title = models.CharField(max_length= 100, blank= False)
    content = models.TextField(max_length= 2000, blank= False)

    original_language = models.ForeignKey(Language, null= True,  on_delete = models.SET_NULL)

    # null = True --> author can be unknown
    author= models.ForeignKey(Author, null = True, on_delete= models.SET_NULL)

    # tuple with choices for translation state
    TRANSLATION_STATE=(('W','Waiting for translation'),
                       ('L','Under revision by administrator'),
                       ('E','Existing translation and editable by authenticated users'),
                       ('V','Final translation NOT editable anymore'),)
    
    status_of_translation = models.CharField(max_length = 1,choices = TRANSLATION_STATE,
                              blank = False, default = 'W',
                              help_text = 'State of traslation')

    class Meta:
        ordering = ['title']
   
    # used for visualization in admin page
    def __str__(self):
        return f'{self.title}'


class Translation(models.Model):
    
    translated_title = models.CharField(max_length=100)   
    translated_content = models.TextField(max_length=2000)
    original_text =models.OneToOneField(Text, null= True,  on_delete = models.SET_NULL)

    creator =models.ForeignKey(User,on_delete = models.SET_NULL,
                                 null = True,blank = True)

    class Meta:
        ordering = ['translated_title']
        permissions = (("permession_of_edit_text_with_every_status", "You can edit every text in every status")
                       ,("edit_W_and_E_status_texts","You can edit W and E text status"))

    # used for visualization in admin page
    def __str__(self):
        return f'{self.translated_title}'

    # used in Translation List to get URL to specific translation
    def get_absolute_url(self):
        return reverse('translation-detail', args=[str(self.id)])




