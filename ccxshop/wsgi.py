#!/usr/bin/env python
# coding: utf-8

# import os
# import sys

# # 将系统的编码设置为UTF8
# reload(sys)
# sys.setdefaultencoding('utf8')

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ccxshop.settings")

# from django.core.handlers.wsgi import WSGIHandler
# application = WSGIHandler()


import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

path = '/home/ccx/project/ccxshop-local/ccxshop'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ccxshop.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())