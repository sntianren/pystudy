#!/usr/bin/env python2
# Filename: backup_ver2.py

import os
import time

# 1. The files and directories to be backed up are specified in alist.
source = ['/home/lao/bin', '/home/lao/list']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or somthing like that

# 2. The backup must be sotred in a main backup directory
target_dir = '/home/lao/Code/python/AByteOfPython/backup/' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Create the subdirectory if isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today

# The name of the zip file
target = today + os.sep + now + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in  a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successfully backup to', target
else:
    print 'Backup FAILED'
