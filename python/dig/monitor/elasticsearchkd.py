#!/usr/bin/python

# 13 February 2015 by Philpot

import sys
import requests
import re

ESPROTOCOL='http'
ESHOST='karma-dig-service.cloudapp.net'
ESPORT=55310
ESPATH='_cat/indices'
VERBOSE=True

error = False
try:
    msg = None
    problems = []
    uri = "%s://%s:%s/%s" % (ESPROTOCOL, ESHOST, ESPORT, ESPATH)
    r = requests.get(uri)
    for line in r.iter_lines():
        fields = re.split(r'''\s+''', line)
        if fields[0] == 'red':
            error = True
            problems.append(line)
    msg = "\n".join(problems)
except Exception as e:
    print >> sys.stderr, e
    error = True
    msg = "get %s failed" % uri

if error:
    if VERBOSE:
        print >> sys.stderr, msg
    sys.exit(1)
else:
    sys.exit(0)
