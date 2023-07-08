from django.urls import path
from . import views

urlpatterns = [path('' , views.index , name='index' ),
               path('authors/', views.AuthorListView.as_view(), name='authors'),
               path('translations/' , views.TranslationListView.as_view() , name='translations' ),
               ]
