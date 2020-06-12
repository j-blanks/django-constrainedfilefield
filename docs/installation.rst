Installation
============


Requirements
------------

-  `Python`_ >= 3.5
-  `Django`_>= 1.11.29
-  `python-magic`_ >= 0.4.2 *iff* you want to check the file type

Note for Python 3.4
^^^^^^^^^^^^^^^^^^^
Shall work with Python 3.4, but not tested in CI as black requires Python>=3.5.


Using PyPI
----------

#. Run

   * ``pip install django-constrainedfilefield``, or
   * ``pip install django-constrainedfilefield[filetype]`` to ensure
     ``python-magic`` is installed.

#. For windows, you must download the dll files and .magic file from
   `pidydx/libmagicwin64`_ (32-bit version on `gnuwin32.sourceforge.net`_),
   add them to ``C:\\Windows\\System32`` (or to a folder in your PATH), and
   set MAGIC_FILE_PATH="..." to the path of your .magic file in your
   settings.py. For more information about the files to download, go to the
   `python-magic help page`_


Using the source code
---------------------

#. Make sure [Pandoc][] is installed
#. Run `./pypi_packager.sh`
#. Run `pip install dist/django_constrainedfilefield-x.y.z-[...].wheel`, where
   `x.y.z` must be replaced by the actual version number and `[...]` depends
   on your packaging configuration
#. For windows, you must download the dll files and .magic file from
   `pidydx/libmagicwin64`_ (32-bit version on `gnuwin32.sourceforge.net`_),
   add them to ``C:\\Windows\\System32`` (or to a folder in your PATH), and
   set MAGIC_FILE_PATH="..." to the path of your .magic file in your
   settings.py. For more information about the files to download, go to the
   `python-magic help page`_



.. _Python:                     https://www.python.org/
.. _Django:                     https://www.djangoproject.com/
.. _python-magic:               https://pypi.org/project/python-magic/
.. _pidydx/libmagicwin64:       https://github.com/pidydx/libmagicwin64
.. _gnuwin32.sourceforge.net:   http://gnuwin32.sourceforge.net/packages/file.htm
.. _python-magic help page:     https://github.com/ahupp/python-magic/blob/43df08c5ed63d7aad839695f311ca1be2eeb1ecb/README.md#dependencies