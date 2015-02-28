#!/usr/bin/python

# 27 February 2015 by Philpot
# possible see https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484


import sys
# import requests
import re
# from requests.auth import HTTPBasicAuth
import json
import subprocess

"""https://darpamemex:darpamemex@isi.memexproxy.com/getSimilar.php?url=https://s3.amazonaws.com/roxyimages/eadc2f6a52936f134cc5b18fe522d5eae83ff6a2.jpg&visualize=1&fast=1&num=100"""

SBPROTOCOL='https'
SBHOST='isi.memexproxy.com'
SBPORT=443
SBPATH="""getSimilar.php?url=https://s3.amazonaws.com/roxyimages/eadc2f6a52936f134cc5b18fe522d5eae83ff6a2.jpg&visualize=0&fast=1&num=5"""
SBUSER='darpamemex'
SBPASSWORD='darpamemex'
VERBOSE=True

SBRESULT = json.loads("""{ "number": 1, "images": [ { "similar_images": { "image_urls": [ null, null, null, null, null ], "cached_image_urls": [ "https://s3.amazonaws.com/roxyimages/eadc2f6a52936f134cc5b18fe522d5eae83ff6a2.jpg", "https://s3.amazonaws.com/roxyimages/85c1b1688af7c615c312b2d90d43f45bcd6a5ccc.jpg", "https://s3.amazonaws.com/roxyimages/843152c8d0077c70a8758fb0532556dfbbc48967.jpg", "https://s3.amazonaws.com/roxyimages/01933324709f4f99253bf5dc55bfe90a463b639f.jpg", "https://s3.amazonaws.com/roxyimages/82c2bb6782e5cd0a97a64b3dcd3e033692231d41.jpg" ], "page_urls": [ null, null, null, null, null ], "cached_page_urls": [ null, null, null, null, null ], "unique_ht_index": [ 7797950, 7397559, 43494696, 27443871, 26070701 ], "sha1": [ "D431422A353C1DF0945BCDEFDEEFA0C15B1F4133", "7EDD45E0489D302466B30C0867F7DC9FFD9ED139", "0E68336EEBAE83A07597B29E8F2BC68C8CA4350B", "6B80365272D8CF1D8D480059F83F6838E3774981", "E09DBA699F3CAEFBA02F0DB579B49D62C706D06E" ], "distance": [ "-5.6054e-07", "2.76939e-05", "0.00441944", "0.0129891", "0.0129965" ] } } ] }""")

SBRESULT = json.loads("""{
    "number": 1, 
    "images": [
        {
            "similar_images": {
                "image_urls": [
                    null, 
                    null, 
                    null, 
                    null, 
                    null
                ], 
                "cached_image_urls": [
                    "https://s3.amazonaws.com/roxyimages/eadc2f6a52936f134cc5b18fe522d5eae83ff6a2.jpg", 
                    "https://s3.amazonaws.com/roxyimages/85c1b1688af7c615c312b2d90d43f45bcd6a5ccc.jpg", 
                    "https://s3.amazonaws.com/roxyimages/843152c8d0077c70a8758fb0532556dfbbc48967.jpg", 
                    "https://s3.amazonaws.com/roxyimages/01933324709f4f99253bf5dc55bfe90a463b639f.jpg", 
                    "https://s3.amazonaws.com/roxyimages/82c2bb6782e5cd0a97a64b3dcd3e033692231d41.jpg"
                ], 
                "page_urls": [
                    null, 
                    null, 
                    null, 
                    null, 
                    null
                ], 
                "cached_page_urls": [
                    null, 
                    null, 
                    null, 
                    null, 
                    null
                ], 
                "unique_ht_index": [
                    7797950, 
                    7397559, 
                    43494696, 
                    27443871, 
                    26070701
                ], 
                "sha1": [
                    "D431422A353C1DF0945BCDEFDEEFA0C15B1F4133", 
                    "7EDD45E0489D302466B30C0867F7DC9FFD9ED139", 
                    "0E68336EEBAE83A07597B29E8F2BC68C8CA4350B", 
                    "6B80365272D8CF1D8D480059F83F6838E3774981", 
                    "E09DBA699F3CAEFBA02F0DB579B49D62C706D06E"
                ], 
                "distance": [
                    "-5.6054e-07", 
                    "2.76939e-05", 
                    "0.00441944", 
                    "0.0129891", 
                    "0.0129965"
                ]
            }
        }
    ]
}""")

def same(a,b):
    return a==b

error = False
try:
    msg = None
    problems = []
    uri = "%s://%s:%s@%s/%s" % (SBPROTOCOL, SBUSER, SBPASSWORD, SBHOST, SBPATH)
    cmd = ["/usr/bin/curl", "-s", "-k", "%s" % uri]
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
