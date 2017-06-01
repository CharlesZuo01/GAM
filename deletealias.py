
import os
import sys

for i in range(1, len(sys.argv)):
	os.system("python GAM-3.7/src/gam.py delete alias " + sys.argv[i])

