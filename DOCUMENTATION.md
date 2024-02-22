# pj_tracoll Documentation

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#e-r-diagram">E-R Diagram</a>
    </li>
    <li>
        <a href="#app-description">App description</a>
   </li>
    <li>
        <a href="#testing-suite">Testing suite</a>
   </li>
  </ol>
</details>

-----------------------------------------------------------------------------------------------------------------------------------------------
## E-R Diagram
![E-R Diagram](/images/E-R-diagram.jpg)

User type is provided by Django: 
https://docs.djangoproject.com/en/4.2/ref/contrib/auth/

-----------------------------------------------------------------------------------------------------------------------------------------------

## App description


URL rules have the following structure:
(string for match test | matched view | url rule name).
Class based views require the as_view() method. All templates inherit from base_generic.html: 
it defines a structure based on a left sidebar, with navigation links between pages. 
On the right there is a div containing a content block, which will be filled by the other
 templates that inherit from it, as well as a pagination block. External CSS files are also imported.

View and URL rules for authentication are added automatically by Django thanks to the instruction:

    urlpatterns += [ path('account/', include('django.contrib.auth.urls')), ]

added in the urls.py file (at project level).

The standard templates supplied by Django have been manually modified, with some graphical 
modifications (the margin of the login page has been modified).


### Homepage
![Homepage](/images/index.jpg)
A) Rule URL: path('' , views.index , name='index')

B) Function-based display: index
Counts occurrences of texts, translations, authors and languages. Update the number 
of visits using cookies (creating the field request.session['num_visits'] if not present). 
The data is saved in a context and passed to the template calling the render function.

C) Template: index.html
It represents an introduction to the application where the number of texts, authors, 
languages ​​(with the display of the flags of the languages ​​present) in the app is 
indicated, and how many visits have been made to the home page, within a table.


### Author list page
![authors_list](/images/authors_list.jpg)
A) Rule URL: path('authors/', views.AuthorListView.as_view(), name='authors')

B) Class based view: AuthorListView
Inherits from Django's ListView class. Model specifies the entity from which the data 
is derived. Paginated_by indicates the number of database records to display for each page.

C) Template: author_list.html
The content block is filled with the list of authors using a for loop. Each entry in the list is a link 
to a detail page of the related author, using the get_absolute_url function (given the author's 
primary key, it returns the URL to the specific detail page).


### Authors detail page

#### when NOT logged in
![author_detail_NOT_logged_in](/images/author_detail_NOT_logged_in.jpg)

#### when logged in
![author_detail_logged_in](/images/author_detail_logged_in.jpg)
A) Rule URL: path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
The author's primary key is passed to URL rule in order to select the correct record in the database.

B) Class based view: AuthorDetailView
Inherits from Django's DetailView class. Model indicates in which table to take the record.
 Get_context_data is overridden. In addition to performing the same functions as the superclass
 method, when the user is NOT authenticated, the number_of_final_texts field (those in state 'V') 
will be added in the context. This is the only type of text that can be displayed in that case. 
For authenticated users all texts by the author are used.

C) Template: author_detail.html
In the content block, author's information and the list of his texts are shown.
If the user is NOT authenticated, it only displays the texts in the 'V' state with a link 
to the translation detail page (using get_absolute_url which returns the URL given the 
translation id), otherwise they are all visible and each entry refers to the specific page 
of the form (texts in state 'E', 'L', 'V' using the translating-page URL rule and passing 
the primary key of the text) or to the translation detail page (ONLY for texts in state 'V ' 
using get_absolute_url which returns the url given the id of the translation). In both cases 
there are appropriate graphical modifications to highlight the state of the text and the links. 
A message warns if the list is empty.

### Translation list page
![final_translations_list](/images/final_translations_list.jpg)
A) Rule URL:
path('translations/' , views.TranslationListView.as_view() , name='translations')

B) Class based view: TranslationListView
Inherits from Django's ListView class. Model indicates the table from which to get the records. 
Paginated_by indicates the number of elements to present per page. Override get_queryset to only 
get text translations in state 'V', this information will be shown to any user in the template.

C) Template: translation_list.html
In the content block, it lists the translations in the final state ('V') also reporting the flags
corresponding to the language of each text. Both the title of the work and the author's name are
 links respectively to the detail page of the author and of the translation (using get_absolute_url,
which given the primary key of the author or of the translation returns the corresponding URL).


### Translation detail page
![final_translaton_detail](/images/final_translaton_detail.jpg)
A) Rule URL:
path('translation/<int:pk>', views.TranslationDetailView.as_view(), name='translation-detail')
The URL rule is passed the translation primary key to select the correct record in the database.

B) Class based view: TranslationDetailView
Inherits from Django's DetailView class. Model indicates in which table to take the record.

C) Template: translation_detail.html
The title and the original content are displayed with the reference language (indicated 
by the flag) compared with the translated ones relating to texts in the final state ('V').

### Form page
![form_page](/images/form_page.jpg)
A) Rule URL: path('translation/<int:pk>/edit/',views.translating_page,name='translating-page')
The URL rule is passed the text primary key to select the correct record in the database.

B) Function based view: translating_page
The user is required to be authenticated (@login_required) and verify that they have permission
 to access this page. The data relating to the text is obtained via the primary key supplied to
 the view and it is checked whether it is a first interaction (HTTP GET) or a subsequent one (HTTP POST):
* HTTP GET: return a form with saved translations (if any) or empty
* HTTP POST: I validate the form with is_valid() (it calls the clean verification methods for
 each field of the form) and I handle the case of correct input (subject to changes) or error.

C) Template: translating_page.html
The form and the title and text in the original language are shown to facilitate translation. 
By checking the permissions, the authenticated NON-administrator user can view the original texts
 in state 'L' WITHOUT the form (which appears for texts in state 'W' and 'E'). 
Administrators, on the other hand, see the texts of all states.

---------------------------------------------------------------------------------------------
## Testing suite

### LogInAndLogOutTest class:
* SetUp: create user to test login and logout

* test_login : by calling the login() function, I simulate a login attempt by a user 
(he accesses the URL rule 'login' which refers him to the login view). This function 
returns True if the login was successful. Check that it returns True.

* test_logout : I log in (see test_login). Then, I call logout(): so the test client 
will have cookies and session data reset to default values. Subsequent requests belong 
to AnonymousUser. In the instance of models.AnonymousUser the is_authenticated field is False. 
I check it in the response obtained after accessing the home page.


### TranslatedTextFormViewTest class:
* setUp : set up method to create user, author, 3 texts and associated translations in 
states W,E,L used in next methods (texts in state V are NOT displayed in the 
form page, but in the translation detail page)

3 methods that check successful access to the form page if authenticated (for each possible text state)

* test_OK_translation_W_form_if_logged_in: login with test_user credentials. 
The get() method simulates an HTTP GET, using the primary key of the test_text to complete the URL.
Thus the URL mapping sends the request to the form view of the corresponding translation.
Check that the authenticated user, by reading the response object, is the same as the test 
one and that the HTTP code is 200, i.e. successful request (OK).

* test_OK_translation_E_form_if_logged_in: same as test_OK_translation_W_form_if_logged_in but with a test_text in state E

* test_OK_translation_L_form_if_logged_in: same as test_OK_translation_W_form_if_logged_in but with a test_text in state L

3 test methods for checking that a NOT authenticated user cannot access the form page (for each possible text state)

* test_302_if_NOT_logged_in_W_text: access with get() the translation page associated with test_test_W 
(using the primary key of the text to construct the URL) without having logged in. Since the @permission_required 
decorator has been added in the associated view (translating_page), the access attempt will result in a redictering 
to the login page and therefore an HTTP 302 code (the page is located at another address, effect of the login redicting). 
Check that the code is 302. However NOT authenticated users cannot log in.

* test_302_if_NOT_logged_in_E_text: same as test_302_if_NOT_logged_in_W_text but with a test_text in state E

* test_302_if_NOT_logged_in_L_text: same as test_302_if_NOT_logged_in_W_text but with a test_text in state L