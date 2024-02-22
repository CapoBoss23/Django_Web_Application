# pj_tracoll_Web_Application

## ATTENTION! THIS REPOSITORY IS ARCHIVED. FEEL FREE TO FORK IF YOU WANT: GIVE CREDIT TO THE ORIGINAL PROJECT AND RESPECT THE LICENSE OF THE PROJECT

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
        <a href="#documentation">Documentation</a>
    </li>
    <li>
        <a href="#built-with">Built With</a>
   </li>
    <li>
        <a href="#prerequisites">Prerequisites</a>
   </li>
   <li> 
        <a href="#getting-started">Getting Started</a>
    </li>
    <li>
        <a href="#license">License</a>
    </li>
    <li>
        <a href="#creators">Creators</a>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### ATTENTION!! THIS PROJECT IS IN DEBUG MODE, IF YOU WANT TO USE IT FOR PRODUCTION FOLLOW THE DEPLOY PROCEDURE:
https://docs.djangoproject.com/en/4.2/howto/deployment/

------------------------------------------------------------------------------
**High level description**

Tracoll is a collaborative translation site of texts in Italian, accessible:
* To one or more administrators of the application
* To one or more authenticated users
* To unauthenticated users


**Data definition**
The necessary data to create TraColl are:

1. a text in the original language is described by:
    * a typology: a text can be a poem or a song
    * a text title (max. 100 characters)
    * a text content (max. 2000 characters)
    * a source language
    * an author, to whom the text is linked
    * a text status, that can be one of these ones: 
        * waiting for translation (W)
        * with translation being reviewed by the administrator (L)
        * with existing translation and collaboratively editable by authenticated users (E)
        * with definitive translation and no longer editable (V). 
    By default, a text without translation will be placed in waiting for translation (W state).

2. an author is described by:
    * a typology: it can be a poet, a songwriter or a band
    * a name  (text of max. 100 characters)

3. the translation of a text is described as follows:
    * the title, translated; textual, of max. 100 characters
    * the content, translated; textual, of max. 2000 characters
    * the original reference text, to which it is uniquely linked
    * the user who generated the translation

4. a language is described by:
    * language name

**Features for application administrators**

An administrator of the application, acting through the administrative page (through the admin address), can:
1. enter data relating to text authors
2. enter lyrics of poems and songs, written by these authors, in one of the languages saved in the application, linking them each to their author

3. decide, for each text, what state it is in: 
    * it is awaiting translation (W)
    * with translation under review (L)
    * with editable translation collaboratively by all users (E)
    * with definitive translation and no longer editable (V)
By default, text with no translation will be pendingtranslation (W state).

4. Edit any existing translations.
5. create users with their authentication passwords
6. add new laguages


**Functionality for generic (unauthenticated) users of the application**

An unauthenticated user of the application can:

1. access homepage which shows the number of texts and authors in the app,
and how many visits were made to the homepage
2. from a side menu, access a page containing the list of authors;
Every list item opens an author detail page. The detail page
of the author reports his information, and the list (as titles) of all texts already
translated (if any exist: otherwise a message is produced saying that none
exist). Each of these titles will be selectable, and in that case a page will appear showing
details of the text, such as its title and content, both in the original and in the
current translation.
3. from the same side menu, access a page showing the list of texts only
translated in the app, each with title and author. Selecting one of such
titles, you can access the translated text details page (see point 2).
4. from the same side menu, access an authentication page (login)

The side menu is always present and available, for all accessed pages.

**Functionality for authenticated users of the application**

An authenticated user must be able to:

1. as the unauthenticated user, access the homepage and the list of
translated texts (points 1 and 3 of the previous section)

2. similar to what happens for unauthenticated users and as described in
point 2 of the previous section, access a page containing the list of
authors, where each element of the list opens a detail page of the author.
However, in this case, the author detail page lists more than just theirs
information, but also the list (as titles) of all the texts, translated or not (if any
exist: otherwise a message is produced saying that none exist).
It is also graphically highlighted whether the text is open to enter or
correct the translation (i.e. in state W or E), or not.
For translated texts that are no longer open to translation, the behavior will be analogous
to that described in point 2 for unauthenticated users: the title will be
selectable and will open a detail page showing the title and content, both in
original and in the current translation.
For texts not yet translated and awaiting translation, as well as for texts for which
the translation exists but can be edited collaboratively, it will also be possible
select the title, and in that case a page will appear showing:
   * the title and content of the text, in the original language
   * an entry form which shows:
     * the current translation of its title (empty if not yet existing)
     * the current translation of its content (empty if not yet existing)

The action of entering a non-empty translation will have the effect of updating the
database and to set the status of the translation to "existing and editable translation" (status E).


3. from the same side menu, access a logout function, which redirects
to the home page (as a user no longer authenticated)

The side menu is always present and available, for each of the pages accessed.

<!-- DOCUMENTATION -->
## Documentation
`DOCUMENTATION.md` explains:
* E-R Diagram
* App description of each page
* Testing suite

<!-- BUILT WITH -->
## Built With

* [Python 3.10.11](https://www.python.org/)
* [Django 4.0](https://www.djangoproject.com/)

<!-- PREREQUISITES -->

### Prerequisites
### ATTENTION!! THIS PROJECT IS IN DEBUG MODE, IF YOU WANT TO USE IT FOR PRODUCTION FOLLOW THE DEPLOY PROCEDURE:
https://docs.djangoproject.com/en/4.2/howto/deployment/


1. #### Python - for Django 4, at least version 3.8 is required
    * ##### Linux (Ubuntu):
        * Usually already installed (under usr/bin )
        * Check: python3 -V
        * Otherwise install: sudo apt install python3
    * ##### macOS:
        * Normally not there (check: python3 -V)
        * Install: from https://www.python.org/downloads/macos/download and run the package
    * ##### Windows (10 or 11):
        * Normally not there (check from cmd line: python3 -V)
        * Install: from https://www.python.org/downloads/windows/download and run the package
        * **Remember to activate the "Add Python to PATH" option**

2. #### Python's pip package manager is also needed
    * ##### Linux (Ubuntu):
        * Normally it's not included. Check: pip3 list
        * Install: sudo apt install python3-pip
    * ##### macOS:
        * Comes with python3 installation
    * ##### Windows (10 or 11):
        * Comes with python3 installation

3. #### Django: installation
    * Manager of virtual environments:
    * Useful for having separate Django environments for different sites

    * ##### Linux (Ubuntu):
        * Install: sudo pip3 install virtualenvwrapper
        * Locate virtualenvwrapper.sh (default: /usr/local/bin)
        * Edit the ~/.bashrc file by adding :

              export WORKON_HOME=$HOME/.virtualenvs
              export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
              export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
              export PROJECT_HOME=$HOME/Devel
              source /usr/local/bin/virtualvwrapper.sh

        * Run it (source ~/.bashrc) or reopen command shell

    * ##### macOS:
        * Install: sudo pip3 install virtualenvwrapper
        * Locate virtualenvwrapper.sh (default: /usr/local/bin)
        * Edit the ~/.bash_profile or ~/.zshrc file by adding:
        
              export WORKON_HOME=$HOME/.virtualenvs
              export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
              export PROJECT_HOME=$HOME/Devel
              source /usr/local/bin/virtualvwrapper.sh

        * Run it with source: eg. source ~/.bash_profile or reopen the command shell

    * ##### Windows (10 o 11):
        * Install: pip3 install virtualenvwrapper-win

4. #### Create virtual environment
    * Create (and log in automatically) a python virtual environment:
    
          mkvirtualenv environment_name
      
    * From here on:
        * to list the virtual environments: workon
        * to enter the environment: workon environment_name
        * to exit: deactivate
        * **We will assume from here on that we are in the virtual environment**

5. #### Install DJango in vitual environment
    * ##### Linux (Ubuntu) or MacOs:
        * Install: pip3 install django~=4.0
        * Check: python3 -m django --version
    * ##### Windows (10 or 11):
        * Install: pip3 install django~=4.0
        * Check: py -3 -m django --version
        * **Note: On Windows, you may need to use py instead of py -3**

6. #### verify the installation by creating a test project:
    * create a folder where you want
    * access it with shell
    * create the site structure using django-admin:
  
          django-admin startproject mytestsite
          cd mytestsite
          python3 manage.py runserver

    * access 127.0.0.1:8000 with your browser to check it' s all ok
    * shut down the server with CTRL-C

**Now you have Django up and running :-)**

<!-- GETTING STARTED -->
## Getting Started

1. Open shell 
2. Create an **empty** folder where the project will be saved
3. Access the folder and fork the repo (you can download zip file if you prefer from code sections of this repository)
 
4. activate you virtual envinroment 
   ```sh
   workon environment_name
   ```
5. makemigrations and migrate
    * #### Windows:
        ```sh
            python manage.py makemigrations
            python manage.py migrate 
        ```
    * #### MacOS or Linux(Ubuntu):
         ```sh
            python3 manage.py makemigrations
            python3 manage.py migrate 
        ```

6. Runserver
   * #### Windows:
        ```sh
            python manage.py runserver
        ```
    * #### MacOS or Linux(Ubuntu):
         ```sh
            python3 manage.py runserver
        ```
If the application starts, you are ok to keep on working on you own! :-)

<!-- LICENSE -->
## License

Distributed under the BSD 3 Clause License. See `LICENSE.txt` for more information.

<!-- CREATORS -->
## Creators

* [CapoBoss23](https://github.com/CapoBoss23)
* [Danksteak](https://github.com/Danksteak)
