|Python| |Django| |License| |PyPIv| |PyPIs| |Build Status| |Coverage
Status| |Documentation Status| |Downloads|

ConstrainedFileField for Django
===============================

This Django app adds a new field type, ``ConstrainedFileField``, that
has the capability of checking the file size and type. Also provides a
javascript checker for the form field.

Features
--------

-  File size limitation
-  File type limitation
-  Javascript file size checker

Documentation
-------------

Docs are available locally or on
`readthedocs.io <https://django-constrainedfilefield.readthedocs.io/>`__.

Note on DOS attacks
-------------------

Important note: the check of the file size is made by Django once the
whole file has been uploaded to the server and stored in a temp
directory (or in memory if the file is small). Thus, this is useful to
guarantee the quota of the users, for example, but will not stop an
attacking user that wants to block the server by sending huge files (e.
g. of several Gb).

To avoid this, you need to configure your front end to limit the size of
uploaded files. How to do it depends on the software you are using. For
example, if you use apache, you should use
`**LimitRequestBody** <http://httpd.apache.org/docs/2.2/mod/core.html#limitrequestbody>`__
directive.

This is a complementary measure, because you'll usually want normal
users that exceed the size by a reasonable amount to get a friendly form
validation message, while attacking users will see how their connection
is abruptly cut before the file finishes uploading. So the recommended
setting is to give ``max_upload_size`` a small value (e.g. 5Mb) and
``LimitRequestBody`` a higher one (e.g. 100Mb).

Credits
-------

This is a fork of
`django-validated-file <https://github.com/kaleidos/django-validated-file>`__
from `Kaleidos <https://github.com/kaleidos>`__.

.. |Python| image:: https://img.shields.io/badge/Python-3.5,3.6,3.7,3.8-blue.svg?style=flat-square
   :target: /
.. |Django| image:: https://img.shields.io/badge/Django-1.11,2.1,2.2-blue.svg?style=flat-square
   :target: /
.. |License| image:: https://img.shields.io/badge/License-BSD--3--Clause-blue.svg?style=flat-square
   :target: /LICENSE
.. |PyPIv| image:: https://img.shields.io/pypi/v/django-constrainedfilefield.svg?style=flat-square
   :target: https://pypi.org/project/django-constrainedfilefield
.. |PyPIs| image:: https://img.shields.io/pypi/status/django-constrainedfilefield.svg
   :target: https://pypi.org/project/django-constrainedfilefield
.. |Build Status| image:: https://travis-ci.org/mbourqui/django-constrainedfilefield.svg?branch=master
   :target: https://travis-ci.org/mbourqui/django-constrainedfilefield
.. |Coverage Status| image:: https://coveralls.io/repos/github/mbourqui/django-constrainedfilefield/badge.svg
   :target: https://coveralls.io/github/mbourqui/django-constrainedfilefield
.. |Documentation Status| image:: https://readthedocs.org/projects/django-constrainedfilefield/badge/?version=latest&style=flat-square
   :target: https://django-constrainedfilefield.readthedocs.io/en/latest/?badge=latest
.. |Downloads| image:: https://pepy.tech/badge/django-constrainedfilefield
   :target: https://pepy.tech/project/django-constrainedfilefield
