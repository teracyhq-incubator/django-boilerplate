django-boilerplate
==================

``django-boilerplate`` promotes best practices to organize and start any Django project.

Continuous Integration
----------------------

|travis build status|_

|jenkins build status|_


Usage
-----

Please head to http://dev.teracy.org/docs/develop/django_training.html

Style checks:

- ``$ pep8 .``

- ``$ pylint --rcfile .pylintrc *.py settings urls apps libs``

- ``$ flake8 --max-complexity 12 .``


Installation
------------

For easy upgrade later, use ``git``:
::
    $ mkdir <your_project>
    $ cd <your_project>
    $ git init
    $ git remote add teracy https://github.com/teracy-official/django-boilerplate
    $ git fetch teracy
    $ git merge teracy/master


Or download zip file from https://github.com/teracy-official/django-boilerplate/archive/master.zip


Contributing
------------

- File issues at https://issues.teracy.org/browse/DJBP

- Follow Teracy's workflow at http://dev.teracy.org/docs/develop/workflow.html


Discussions
-----------

Join us:

- https://groups.google.com/forum/#!forum/teracy

- https://www.facebook.com/groups/teracy

Get our news:

- https://www.facebook.com/teracy.official

- https://twitter.com/teracy_official


Author and contributors
-----------------------

See more details at `AUTHORS.md` and `CONTRIBUTORS.md` files.


License
-------

BSD License
::
    Copyright (c) Teracy, Inc. and individual contributors.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

        1. Redistributions of source code must retain the above copyright notice,
           this list of conditions and the following disclaimer.

        2. Redistributions in binary form must reproduce the above copyright
           notice, this list of conditions and the following disclaimer in the
           documentation and/or other materials provided with the distribution.

        3. Neither the name of Teracy, Inc. nor the names of its contributors may be used
           to endorse or promote products derived from this software without
           specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

.. |travis build status| image:: https://travis-ci.org/teracy-official/django-boilerplate.png?branch=develop
.. _travis build status: https://travis-ci.org/teracy-official/django-boilerplate

.. |jenkins build status| image:: https://ci.teracy.org/buildStatus/icon?job=django-boilerplate-develop
.. _jenkins build status: https://ci.teracy.org/job/django-boilerplate-develop/
