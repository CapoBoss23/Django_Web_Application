from django.urls import path
from . import views

urlpatterns = [path('' , views.index , name='index' ),
               path('authors/', views.AuthorListView.as_view(), name='authors'),
               path('translations/' , views.TranslationListView.as_view() , name='translations' ),
               path('translation/<int:pk>', views.TranslationDetailView.as_view(), name='translation-detail'),
               path('translation/<int:pk>/edit/',views.translating_page,name='translating-page'),
               path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
               ]
               




