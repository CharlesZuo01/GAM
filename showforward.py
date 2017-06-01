#shows users who are forwarding their email

import os
import sys


os.system("python GAM-3.7/src/gam.py all users show forward  | grep True")