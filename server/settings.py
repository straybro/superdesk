#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import os
from pathlib import Path


def env(variable, fallback_value=None):
    env_value = os.environ.get(variable, '')
    if len(env_value) == 0:
        return fallback_value
    else:
        if env_value == "__EMPTY__":
            return ''
        else:
            return env_value


ABS_PATH = str(Path(__file__).resolve().parent)

init_data = Path(ABS_PATH) / 'data'
if init_data.exists():
    INIT_DATA_PATH = init_data

INSTALLED_APPS = [
    'apps.languages',
    'ansa.analysis',
    'ansa.search',
    'ansa.parser',
]


RENDITIONS = {
    'picture': {
        'thumbnail': {'width': 220, 'height': 120},
        'viewImage': {'width': 640, 'height': 640},
        'baseImage': {'width': 1400, 'height': 1400},
    },
    'avatar': {
        'thumbnail': {'width': 60, 'height': 60},
        'viewImage': {'width': 200, 'height': 200},
    }
}

WS_HOST = env('WSHOST', '0.0.0.0')
WS_PORT = env('WSPORT', '5100')

LOG_CONFIG_FILE = env('LOG_CONFIG_FILE', 'logging_config.yml')

REDIS_URL = env('REDIS_URL', 'redis://localhost:6379')
if env('REDIS_PORT'):
    REDIS_URL = env('REDIS_PORT').replace('tcp:', 'redis:')
BROKER_URL = env('CELERY_BROKER_URL', REDIS_URL)

# 5y
CONTENT_EXPIRY_MINUTES = 60 * 24 * 365 * 5

NO_TAKES = True

ANSA_ANALYSIS_URL = "http://172.20.14.51:8080/extractionservice/"

DEFAULT_SOURCE_VALUE_FOR_MANUAL_ARTICLES = 'ANSA'
ORGANIZATION_NAME = 'Agenzia Nazionale Stampa Associata'
ORGANIZATION_NAME_ABBREVIATION = 'ANSA'
NEWSML_PROVIDER_ID = 'ANSA'

LANGUAGES = [
    {'language': 'it', 'label': 'Italiano', 'source': True, 'destination': False},
    {'language': 'en', 'label': 'English', 'source': True, 'destination': False},
]
