#creates group in Google

import os
import sys

if len(sys.argv) != 2:
	print "you can only create one group at a time, please enter the group name as the only argument"
	exit()

os.system("python GAM-3.7/src/gam.py create group " + sys.argv[1])