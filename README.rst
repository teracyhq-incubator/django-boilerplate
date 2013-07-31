===========================
teracy - get project booted
===========================

This project template is the starting point to develop any Django project. It offers best practices to organize project
structure.

Getting started
---------------

1. `Setup working environment and start developing a Django application <https://github.com/teracy-official/teracy-dev/blob/master/README.rst>`_

How to
------

1. Start a new project
::
    $ mkdir cool_project
    $ cd cool_project
    $ git init
    $ git remote add teracy git@github.com:teracy-official/teracy-django-boilerplate.git
    $ git fetch teracy
    $ git merge teracy/master

2. Update to follow teracy's project change
::
    $ git fetch teracy
    $ git merge teracy/master

3. Start a new application
::
    $ cd apps
    $ ../manage.py startapp cool_app


4. Deploy on heroku
::
    $ heroku config:add DJANGO_SETTINGS_MODULE=settings.prod

5. Deploy on openshift

Problems, want to help each other?
----------------------------------

During the development and learning, you're welcome to join us with discussions at https://groups.google.com/forum/#!forum/teracy

Frequently asked questions
--------------------------