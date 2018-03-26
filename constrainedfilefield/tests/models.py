from django.db import models

from constrainedfilefield.fields import ConstrainedFileField, ConstrainedFilePathField


class TestModel(models.Model):
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png'],
        max_upload_size=10240)
    the_file_path = ConstrainedFilePathField(
        null=True,
        blank=True,
        path='testfile',
        content_types=['image/png'],
        max_upload_size=10240)


class TestModelJs(models.Model):
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile',
        content_types=['image/png'],
        max_upload_size=10240,
        js_checker=True)
    the_file_path = ConstrainedFilePathField(
        null=True,
        blank=True,
        path='testfile',
        content_types=['image/png'],
        max_upload_size=10240,
        js_checker=True)


class TestModelNoValidate(models.Model):
    the_file = ConstrainedFileField(
        null=True,
        blank=True,
        upload_to='testfile')
    the_file_path = ConstrainedFilePathField(
        null=True,
        blank=True,
        path='testfile')
