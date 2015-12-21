Change Log
==========

[0.4.0][] (2015-12-21)
----------------------

lots of improvements with broken changes.


- Improvement
    + [DJBP-22] - should organize settings module better #13
    + [DJBP-23] - should organize urls module better #15
    + [DJBP-24] - audit the settings and overall organization to keep up to date with Django 1.8.x #16
    + [DJBP-25] - migrate Site data for dev, stag and prod modes #19
    + [DJBP-27] - should support send mass html mails #21
    + [DJBP-28] - should support optional celery app #24
    + [DJBP-30] - should support newrelic monitoring #22


- Task
    + [DJBP-26] - Release django-boilerplate v0.4.0


[0.3.0][] (2015-12-01)
----------------------

upgrade Django and packages, add apps and libs to the sytem path

- Bug
    + [DJBP-19] - Fix style error from travis-ci failed build


- Improvement
    + [DJBP-18] - add apps and libs to system path


- Task
    + [DJBP-20] - upgrade dependencies


[0.2.0][] (2013-11-07)
----------------------

proper prod settings, improve jenkins.sh, remove "test" profile settings.

- Improvement
    + [DJBP-7] - import TEMPLATE_CONTEXT_PROCESSORS on settings.dev
    + [DJBP-8] - proper prod settings
    + [DJBP-9] - test requirements and settings are not really needed, remove it
    + [DJBP-13] - Improve jenkins.sh

- Task
    + [DJBP-10] - installation bash script for overlay upgrade strategy project
    + [DJBP-11] - upgrade to latest django 1.5.x
    + [DJBP-12] - set email_backend to be console email backend for dev mode


[0.1.0][] (2013-09-07)
----------------------

Initial milestone release

- separated boilerplate stuff and project specific stuff

- coding convention checking, unit test, test coverage report


[0.1.0]: https://issues.teracy.org/secure/ReleaseNote.jspa?projectId=10407&version=10007

[0.2.0]: https://issues.teracy.org/secure/ReleaseNote.jspa?projectId=10407&version=10200

[0.3.0]: https://issues.teracy.org/secure/ReleaseNote.jspa?projectId=10407&version=10501

[0.4.0]: https://issues.teracy.org/secure/ReleaseNote.jspa?projectId=10407&version=12500
