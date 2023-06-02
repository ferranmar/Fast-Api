import os
from core.utils import secretmanager

# ENV VARS
ORIGINS = os.environ.get('ORIGINS', '*')
API_VERSION = os.environ.get('API_VERSION', '/api/v1')

# PROJECT
PROJECT = os.environ.get('PROJECT', 'gts-atr3-sbox')
TITLE = os.environ.get('TITLE', 'FAST API CLOUD RUN')
VERSION = os.environ.get('VERSION', '1.0.0')

# ORACLE DATABASE
ORACLE_USER = os.environ.get('ORACLE_USER', 'CONT_MON')
ORACLE_PSW = os.environ.get('ORACLE_PSW', secretmanager.secret_manager('ORACLE_PSW'))
ORACLE_HOST = os.environ.get('ORACLE_HOST', '172.20.32.36')
ORACLE_PORT = os.environ.get('ORACLE_PORT', '1567')
ORACLE_DB = os.environ.get('ORACLE_DB', 'SIOM')
ORACLE_TYPE = os.environ.get('ORACLE_TYPE', 'SID')
