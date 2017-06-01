#add a user to multiple groups, arguments are user@domain.com group1 group2 group3 etc...

import os
import sys

for i in range(2, len(sys.argv)):
	os.system("python GAM-3.7/src/gam.py update group " + sys.argv[i] + " add member user " + sys.argv[1])

