import os
import sys

if len(sys.argv) != 4:
	print "Please enter email without the @domain.com, firstname, lastname in that order"
	exit()

password = str(os.system("pwgen -c -n 10 1"))
os.system("python GAM-3.7/src/gam.py create user " + sys.argv[1] + ' firstname '\
+ sys.argv[2] + ' lastname ' + sys.argv[3] + ' password ' + password)


