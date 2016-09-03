# -*- coding:utf-8 -*-
from file_uploader.settings import *
import os

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
COVERAGE_REPORT_HTML_OUTPUT_DIR = '.cover'

NOSE_ARGS = [
    '--with-xunit',
    '--with-coverage',
    '--cover-xml',
    '--cover-html',
    '--cover-package=upload_form',
]

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'test.db'),
    }
}
