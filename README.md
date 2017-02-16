[![Python](https://img.shields.io/badge/Python-3.5-blue.svg?style=flat-square)](/)
[![Django](https://img.shields.io/badge/Django-1.10-blue.svg?style=flat-square)](/)
[![License](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg?style=flat-square)](/LICENSE)

# ConstrainedFileField for Django

This Django app adds a new field type, `ConstrainedFileField`, that has the
capability of checking the document size and type. Also provides a javascript checker for the 
form field.

## Installation

 * Download and install package with `python setup.py install`.
 * Add `constrainedfilefield` to the `INSTALLED_APPS` in your project's settings (usually `settings
 .py`)
 
**Note** that this package depends on `python-magic` if you want to check the document type.

## Validate single file

Create a model and add a field of type `ConstrainedFileField`. You can add a maximum size in bytes
and a list of valid mime types that will be allowed. The list of all mime types is available
here: http://www.iana.org/assignments/media-types/index.html.
Setting none of the above, it behaves like a regular `FileField`.
```
from django.db import models
from constrainedfilefield.fields import ConstrainedFileField

class TestModel(models.Model):
    the_file = ConstrainedFileField(
                    null = True,
                    blank = True,
                    upload_to = 'testfile',
                    max_upload_size = 10240,
                    content_types = ['image/png'])
```

The field can be used in forms or model forms like a normal `FileField`. If a user tries to upload
a file which is too large or without a valid type, a form validation error will occur.

Additionally, to prevent user uploading too large files, a javascript checker can be set to the 
form field. In order to achieve that, you need to include the javascript in the template where the
form field is used

    {% load static %}
    <script src="{% static "constrainedfilefield/js/file_checker.js" %}"></script>

and activate this feature by setting `js_checker=True` when instantiating the 
`ConstrainedFileField`.

## Note on DOS attacks

Important note: the check of the file size is made by Django once the whole file has been uploaded
to the server and stored in a temp directory (or in memory if the file is small). Thus, this is
useful to guarantee the quota of the users, for example, but will not stop an attacking user that
wants to block the server by sending huge files (e. g. of several Gb).

To avoid this, you need to configure your front end to limit the size of uploaded files. How to do
it depends on the software you are using. For example, if you use apache, you should use
**LimitRequestBody** directive (http://httpd.apache.org/docs/2.2/mod/core.html#limitrequestbody).

This is a complementary measure, because you'll usually want normal users that exceed the size by a
reasonable amount to get a friendly form validation message, while attacking users will see how their
connection is abruptly cut before the file finishes uploading. So the recommended setting is to give
`max_upload_size` a small value (e.g. 5Mb) and `LimitRequestBody` a higher one (e.g. 100Mb).

