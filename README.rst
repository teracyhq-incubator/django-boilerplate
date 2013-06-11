==============================
teracy - Django project layout
==============================


How to start with this project layout
-------------------------------------

1. Create a virtual environment by installing virtualenvwrapper here: http://virtualenvwrapper.readthedocs.org/en/latest/

2. ``workon`` that created virtual environment.

3. Clone this repository to your workspace.

4. Install dev dependency requirements with this command: `pip install -r requirements/dev.txt`.

5. Syncdb with: ``python manage.py syncdb`` and start the server with ``python manage.py runserver``.

It's time having fun for developing cool apps :-).


How to start develop an application from this project layout
------------------------------------------------------------

From that clone repository as mentioned above, for example, we need to create a ``cool`` application under `apps` directory, just ``cd apps`` then ``django-amdin.py startapp cool``.

That's it. Happy coding :-)!


Work with SASS
--------------

1. Requirements: install ``compass`` (require ``sass``) with: ``gem install sass`` and ``gem install compass``.
It's recommended to install ``virtualenvwrapper.gem`` at https://pypi.python.org/pypi/virtualenvwrapper.gem

2. Watch any working compass projects with: ``sh compass.sh``.

3. The compass project should be created into ``static`` directory and maps compiled assets into ``../css``, ``../img``
and ``../js`` respectively.
::
    compass create compass --css-dir "../static/css" --javascripts-dir "../static/js" --images-dir "../static/img"

3. Whenever a compass is created, add its project path to compass.sh for easier watching.


How to deploy on heroku
-----------------------
+ heroku config:add DJANGO_SETTINGS_MODULE=settings.prod


How to deploy on openshift
--------------------------