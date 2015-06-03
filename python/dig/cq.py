#!/usr/bin/python

import sys, cbor, json
from subprocess import Popen, PIPE, STDOUT

## emulate 'jq' argument pattern
## no options for now

fltr=sys.argv[1]

try:
    input=sys.argv[2]
except IndexError:
    input=sys.stdin

with open(input, 'rb') as f:
    data = json.dumps(cbor.load(f))
    p = Popen(['jq', fltr], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    # jq_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
    input = data.decode('utf-8')
    # all = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')
    all = p.communicate(input=input)
    jq_stdout = all[0]
    sys.stdout.write(jq_stdout.decode())


