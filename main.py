print "hello world"

import os, sys

path, dirs, files = next(os.walk("./"))
file_count = len(files)

if file_count >= 2:
  print "it's getting busy"
  sys.exit(1)
else:
  print "it's nice an quiet"