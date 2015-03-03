#!/usr/bin/python

# 27 February 2015 by Philpot
# possible see https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484

"""https://simbroker.memexproxy.com/ds/similar/images?uri=https://www.google.com/images/srpr/logo11w.png"""

import sys
import re
import json
import subprocess

SIMPROTOCOL='https'
SIMHOST='simbroker.memexproxy.com'
SIMPORT=443
SIMIMAGE="""https://www.google.com/images/srpr/logo11w.png"""
# SIMIMAGE="bobo"
SIMPATH="""ds/similar/images?uri=%s""" % SIMIMAGE
SIMUSER='memex'
SIMPASSWORD='digdig'
VERBOSE=True

import util

@util.echo
def correct(j):
    if j.get("ad_uri"):
        return True
    else:
        raise ValueError("bad value %s" % j)

error = False
try:
    msg = None
    problems = []
    uri = "%s://%s:%s@%s/%s" % (SIMPROTOCOL, SIMUSER, SIMPASSWORD, SIMHOST, SIMPATH)
    cmd = ["/usr/bin/curl", "-s", "-k", "%s" % uri]
    print cmd
    output = subprocess.check_output(cmd)
    print output
    if correct(json.loads(output)):
        pass
    else:
        problems.append("failed")
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
