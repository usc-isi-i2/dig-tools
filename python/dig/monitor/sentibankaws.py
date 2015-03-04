#!/usr/bin/python

# 27 February 2015 by Philpot
# possible see https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484
# 3 March 2015 adapted from sentibankdt

import sys
import re
import json
import subprocess

"""http://sentibank.zapto.org/getSimilar.php?url=https://s3.amazonaws.com/roxyimages/cf9c3daca792f5bdf1b65ba1b592815b8aeeefe9.jpg&visualize=0&num=5&fast=1"""

SBPROTOCOL='http'
SBHOST='sentibank.zapto.org'
SBPATH="""getSimilar.php?url=https://s3.amazonaws.com/roxyimages/eadc2f6a52936f134cc5b18fe522d5eae83ff6a2.jpg&visualize=0&fast=1&num=5"""
VERBOSE=True

SBRESULT = json.loads("""{ "number": 1, "images": [ { "similar_images": { "image_urls": [ null, null, null, null, null ], "cached_image_urls": [ "https://s3.amazonaws.com/roxyimages/cmuImages/Texas_2013_6_27_1372357054000_5_4.jpg", "https://s3.amazonaws.com/roxyimages/2a98117ba39d6ac8de7e8c7d7b8b532167930e11.jpg", "https://s3.amazonaws.com/roxyimages/55258a7fe329c586888946d510047e0f6c9030ab.jpg", "https://s3.amazonaws.com/roxyimages/0a06084d44a73ce2035674bef1b3c56e477cf8e3.jpg", "https://s3.amazonaws.com/roxyimages/8a58dbfc8713214ad34741e82c6f013c7b913e56.jpg" ], "page_urls": [ null, null, null, null, null ], "cached_page_urls": [ null, null, null, null, null ], "unique_ht_index": [ 2945461, 1120697, 6116613, 35479660, 5160106 ], "sha1": [ "C5299FFC8919F1019D40C2D28393ED6D03FC45EF", "1C2944C33D532564FDF81C5B243CEDFA9D3BF405", "7E8736AE5D6581E123B1EEA539F96269EBCC9992", "8817ADA6123F93BB916E9AFB5B7BACA34A570FE3", "E749EAD9823E58BFC00635270E8E3800BE2EEEF8" ], "distance": [ "0.21791", "0.223648", "0.305206", "0.321613", "0.32398" ] } } ] }""")

def same(a,b):
    return a==b

error = False
try:
    msg = None
    problems = []
    uri = "%s://%s/%s" % (SBPROTOCOL, SBHOST, SBPATH)
    cmd = ["/usr/bin/curl", "-s", "%s" % uri]
    output = subprocess.check_output(cmd)
    if same(json.loads(output), SBRESULT):
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
