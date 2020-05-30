Usage
============


Validate single file
--------------------

The field can be used in forms or model forms like a normal ``FileField``. If
a user tries to upload a file which is too large or without a valid type, a
form validation error will occur.

Note that the validation does not occur on the field itself (on ``save()``),
but when validated through a form.

Creating form from model
^^^^^^^^^^^^^^^^^^^^^^^^

Create a model and add a field of type ``ConstrainedFileField``. You can add a
maximum size in bytes and a list of valid mime types that will be allowed. The
list of all mime types is provided by the `IANA`_.
Setting none of the above, it behaves like a regular ``FileField``::

    from django.db import models
    from constrainedfilefield.fields import ConstrainedFileField

    class TestModel(models.Model):
        the_file = ConstrainedFileField(
                                null=True,
                                blank=True,
                                upload_to='testfile',
                                content_types=['image/png'],
                                max_upload_size=10240
                                        )


::

    from django import forms
    from myproject.models import TestModel

    class TestModelForm(forms.ModelForm):
        class Meta:
            model = TestModel
            fields = ['the_file']


Building a form
^^^^^^^^^^^^^^^

::

    from django import forms
    from constrainedfilefield.fields import ConstrainedFileField

    class TestNoModelForm(forms.Form):
        the_file = ConstrainedFileField(
                        null=True,
                        blank=True,
                        upload_to='testfile',
                        content_types=['image/png'],
                        max_upload_size=10240
                                        ).formfield()


Javascript file size validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Additionally, to prevent user uploading too large files, a javascript checker can be set to the
form field. In order to achieve that, you need to

#. Add ``constrainedfilefield`` to the ``INSTALLED_APPS``. This will load the
   javascripts from the static files.
#. Activate this feature by setting ``js_checker=True`` when instantiating the
   ``ConstrainedFileField``.
#. Include the javascript in the template where the form field is used::

    {% load static %}
    <script src="{% static 'constrainedfilefield/js/file_checker.js' %}"></script>


Validate single image
---------------------

Same as above, using ``ConstrainedImageFileField`` instead.

The ``ConstrainedImageField`` offers additional constraints:

* ``min_upload_size`` to define minimal file size.
* ``[min|max]_upload_[width|height]`` to define min/max dimensions, respectively width and height.


.. _IANA:   http://www.iana.org/assignments/media-types/index.html