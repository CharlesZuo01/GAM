#Delete a user

import os
import sys



os.system("python GAM-3.7/src/gam.py delete user " + sys.argv[1])

print "you deleted " + sys.argv[1] + "@zuolabs.com"