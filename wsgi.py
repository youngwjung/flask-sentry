#!/usr/bin/env python

import sys
import site

site.addsitedir('/usr/local/lib/python3.7/site-packages')
site.addsitedir('/usr/local/lib64/python3.7/site-packages')

sys.path.insert(0, '/var/www/html')

from app import app as application