#transfers drive ownership from email1 to email2

import os
import sys

#in case you screw up and transfer the wrong way
#if sys.argv[1] == 'youraccount@domain.com':
	#print "Owner should be second argument, not first."
	#exit()

os.system("python GAM-3.7/src/gam.py user " + sys.argv[1] + " transfer drive " + sys.argv[2])

print "You transferred docs belonging to" + sys.argv[1] + " to " + sys.argv[2]