#!/usr/bin/env python

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

lout = re.split(r"\W+",line)

print(lout)