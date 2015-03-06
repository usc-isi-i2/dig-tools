#!/usr/bin/python

# 27 February 2015 by Philpot
# possible see https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484
# 3 March

"""http://simbroker.dig.isi.edu:9091/ds/similar/images?uri=https://www.google.com/images/srpr/logo11w.png"""

import sys
import re
import json
import subprocess

SIMPROTOCOL='http'
SIMHOST='simbroker.dig.isi.edu'
SIMPORT=9091
SIMIMAGE="""https://www.google.com/images/srpr/logo11w.png"""
# SIMIMAGE="bobo"
SIMPATH="""ds/similar/images?uri=%s""" % SIMIMAGE
SIMUSER='memex'
SIMPASSWORD='digdig'
VERBOSE=True

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
    output = subprocess.check_output(cmd)
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
