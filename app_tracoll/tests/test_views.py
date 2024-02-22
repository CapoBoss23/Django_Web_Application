from django.test import TestCase
from app_tracoll.forms import TranslatedTextForm
from django.urls import reverse
from django.contrib.auth.models import Permission
from app_tracoll.models import Author, Text, Translation, Language
from django.contrib.auth.models import User
from django.urls import reverse

class LogInAndLogOutTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='user1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_login(self):
        login = self.client.login (username='user1',password='1X<ISRUkw+tuK')
        # login() returns True if it the credentials were accepted and login was successful. 
        # source: https://docs.djangoproject.com/en/4.2/topics/testing/tools/#django.test.Client.login
        self.assertTrue(login)

    def test_logout(self):
        login = self.client.login (username='user2',password='1X<ISRUkw+tuKfsfsfs')

        # After you call this method, the test client will have all the cookies and session data cleared to defaults. 
        # Subsequent requests will appear to come from an AnonymousUser.
        # source: https://docs.djangoproject.com/en/4.2/topics/testing/tools/#django.test.Client.logout
        # ----------------------------------------------------------------
        # in class models.AnonymousUser is_authenticated is False instead of True. -> we check this field
        # source: https://docs.djangoproject.com/en/4.2/ref/contrib/auth/#anonymoususer-object
        self.client.logout()

        # NEED TO GET THIS DATA BY HTTP RESPONSE 
        # try access home page and check that user is NOT authenticated :
        response = self.client.get (reverse('index'))

        self.assertFalse(response.context['user'].is_authenticated)


class TranslatedTextFormViewTest(TestCase):
    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------

    # set up method that creates data used for tets
    def setUp(self):
        #----------------------------------------------------------------------------------
        # Create user, since page is login-restricted 
        test_user1 = User.objects.create_user(username='user1', password='1X<ISRUkw+tuK')
        
        # take 2 permissions for normal authenticated users 
        permission_read = Permission.objects.get(name='You can watch every text status') 
        permission_W_E_edit = Permission.objects.get(name='You can edit W and E text status') 

        # give permissions to desired user
        test_user1.user_permissions.add(permission_read)
        test_user1.user_permissions.add(permission_W_E_edit)
        test_user1.save()
        #----------------------------------------------------------------------------------

        # add author that user will use in tests
        test_author = Author.objects.create(type_of_author='P', name_of_author='author') 
        test_author.save()

        # add language that user will use in tests
        test_language = Language.objects.create(name_of_language='language') 
        test_language.save()

        #----------------------------------------------------------------------------------
        # add traslation for texts with different status_of_translation used in tests

        text_translation_E = Translation(translated_title="translated_title_E", translated_content="translated_content_E", 
                                       original_text= None, creator = test_user1)
        text_translation_E.save()

        text_translation_L = Translation(translated_title="translated_title_L", translated_content="translated_content_L", 
                                       original_text= None, creator = test_user1)
        text_translation_L.save()

        #----------------------------------------------------------------------------------
        # add texts that will be used in tests
        test_text_W = Text.objects.create(type_of_text='P', title='title', content='content', original_language=test_language,
                                        author =test_author, status_of_translation = 'W') 
        test_text_W.save()

        #----------------------------------------------------------------------------------
        test_text_E = Text.objects.create(type_of_text='P', title='title', content='content', original_language=test_language,
                                        author =test_author, status_of_translation = 'E') 
        test_text_E.save()
        # link translation to text
        text_translation_E.original_text = test_text_E 
        text_translation_E.save()

        #----------------------------------------------------------------------------------
        test_text_L = Text.objects.create(type_of_text='P', title='title', content='content', original_language=test_language,
                                        author =test_author, status_of_translation = 'L') 
        test_text_L.save()
        # link translation to text
        text_translation_L.original_text = test_text_L
        text_translation_L.save()
        
        #----------------------------------------------------------------------------------

        # save data in order to be called in test methods
        self.test_text_W = test_text_W
        self.test_text_E = test_text_E
        self.test_text_L = test_text_L

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    # tests to check if logged-in user can acces form page (HTTP code 200 = ok)

    def test_OK_translation_W_form_if_logged_in(self):
        # login with test user credentials
        login = self.client.login(username='user1', password='1X<ISRUkw+tuK')
        # use HTTP get to reach desired page
        response = self.client.get('/app_tracoll/translation/'+ str(self.test_text_W.pk) +'/edit/')

        # check if logged-in user is test_user1
        self.assertEqual(str(response.context['user']),'user1')
        # check HTTP 200 = OK
        self.assertEqual(response.status_code, 200)

    def test_OK_translation_E_form_if_logged_in(self):
        # login with test user credentials
        login = self.client.login(username='user1', password='1X<ISRUkw+tuK')
        # use HTTP get to reach desired page
        response = self.client.get('/app_tracoll/translation/'+ str(self.test_text_E.pk) +'/edit/')

        #check if logged-in user is test_user1
        self.assertEqual(str(response.context['user']),'user1')
        # check HTTP 200 = OK
        self.assertEqual(response.status_code, 200)

    def test_OK_translation_L_form_if_logged_in(self):
        # login with test user credentials
        login = self.client.login(username='user1', password='1X<ISRUkw+tuK')
        # use HTTP get to reach desired page
        response = self.client.get('/app_tracoll/translation/'+ str(self.test_text_L.pk) +'/edit/')

        #check if logged-in user is test_user1
        self.assertEqual(str(response.context['user']),'user1')
        # check HTTP 200 = OK
        self.assertEqual(response.status_code, 200)

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------
    # tests to check if NOT logged-in user can acces form page (HTTP code 302 = FOUND redirect code, 
    # because of decorator @login_required). However, user CANNOT acces form page

    # as translating_page.html has decorator @login_required, NOT 
    # logged-in user will be redirected to login page. So this user 
    # CANNOT enter form page and 302 HTTP code is returned 
    def test_302_if_NOT_logged_in_W_text(self): 
        # access attempt to form page by a not logged-in user
        response = self.client.get('/app_tracoll/translation/'+ str(self.test_text_W.pk) +'/edit/')

        # check HTTP 302 = resource requested is found, BUT users (beacuse 
        # of decorator @login_required) is redirected to login page)
        self.assertEqual(response.status_code, 302) 


    # as translating_page.html has decorator @login_required, NOT 
    # logged-in user will be redirected to login page. So this user 
    # CANNOT eneter form page and 302 HTTP code is returned 
    def test_302_if_NOT_logged_in_E_text(self): 
        # access attempt to form page by a not logged-in user
        response = self.client.get('/app_tracoll/translation/'+ str(self.test_text_E.pk) +'/edit/')

        # check HTTP 302 = resource requested is found, BUT users (beacuse 
        # of decorator @login_required) is redirected to login page
        self.assertEqual(response.status_code, 302) 


    # as translating_page.html has decorator @login_required, NOT 
    # logged-in user will be redirected to login page. So this user 
    # CANNOT eneter form page and 302 HTTP code is returned 
    def test_302_if_NOT_logged_in_L_text(self): 
        # access attempt to form page by a not logged-in user
        response = self.client.get('/app_tracoll/translation/'+ str(self.test_text_L.pk) +'/edit/')

        # check HTTP 302 = resource requested is found, BUT users (beacuse 
        # of decorator @login_required) is redirected to login page
        self.assertEqual(response.status_code, 302) 

    #---------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------