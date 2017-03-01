#!/usr/bin/env python
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

if __name__ == "__main__":
    import sys
    from django import setup
    from django.test.runner import DiscoverRunner

    setup()
    sys.exit(DiscoverRunner(verbosity=1).run_tests(['constrainedfilefield']))
