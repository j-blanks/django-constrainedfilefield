#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'constrainedfilefield.tests.settings'

if __name__ == "__main__":
    # https://docs.djangoproject.com/en/1.8/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage
    import django

    django.setup()

    import sys
    from django.test.runner import DiscoverRunner

    sys.exit(DiscoverRunner(verbosity=1).run_tests(['constrainedfilefield']))
