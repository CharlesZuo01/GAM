
import os
import sys

for i in range(2, len(sys.argv)):
	os.system("python GAM-3.7/src/gam.py create alias " + sys.argv[i] + " user " + sys.argv[1])
