#transfers drive ownership from email1 to email2

import os
import sys

#Owner should be second argument, with the account being transferred the first 

os.system("python GAM-3.7/src/gam.py user " + sys.argv[1] + " transfer drive " + sys.argv[2])

print "You transferred docs belonging to" + sys.argv[1] + " to " + sys.argv[2]
