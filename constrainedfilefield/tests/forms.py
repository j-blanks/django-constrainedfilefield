from django import forms

from constrainedfilefield.tests.models import TestModel, TestModelJs, TestModelNoValidate


class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['the_file', 'the_file_path']


class TestModelFormJs(forms.ModelForm):
    class Meta:
        model = TestModelJs
        fields = ['the_file', 'the_file_path']


class TestModelNoValidateForm(forms.ModelForm):
    class Meta:
        model = TestModelNoValidate
        fields = ['the_file', 'the_file_path']


class TestNoModelForm(forms.Form):
    from constrainedfilefield.fields import ConstrainedFileField, ConstrainedFilePathField
    the_file = ConstrainedFileField(null=True,
                                    blank=True,
                                    upload_to='testfile',
                                    content_types=['image/png'],
                                    max_upload_size=10240).formfield()
    the_file_path = ConstrainedFilePathField(null=True,
                                             blank=True,
                                             path='testfile',
                                             content_types=['image/png'],
                                             max_upload_size=10240).formfield()


class TestNoModelJsForm(forms.Form):
    from constrainedfilefield.fields import ConstrainedFileField, ConstrainedFilePathField
    the_file = ConstrainedFileField(null=True,
                                    blank=True,
                                    upload_to='testfile',
                                    content_types=['image/png'],
                                    max_upload_size=10240,
                                    js_checker=True).formfield()
    the_file_path = ConstrainedFilePathField(null=True,
                                             blank=True,
                                             path='testfile',
                                             content_types=['image/png'],
                                             max_upload_size=10240,
                                             js_checker=True).formfield()
