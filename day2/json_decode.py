#!/usr/bin/env python

import json
import sys

jsonData = '{"storage-driver": "devicemapper","storage-opts":["dm.thinpooldev=/dev/mapper/docker-thinpool","dm.use_deferred_removal=true","dm.use_deferred_deletion=true"]}'
text = json.loads(jsonData)

def json_decode(jcode,put):
    print(jcode[put])

json_decode(text,sys.argv[1])