#!/usr/bin/env python3

#####################################################################
#####################################################################
## @author: kimitonana
## @description: Nemo Action: 
##   rename file with a randomized name
##
##   0001.JPG
##   -->
##   blablawesh.jpg
##
#####################################################################
#####################################################################

import os
import sys
import string
import random
import time

LOGFILE = '/tmp/give_random_name_renaming.log'
CHAR    = string.ascii_lowercase + string.digits
LENGTH  = 10

def shuffle():
  shuffle = ''
  for i in range(0, LENGTH):
    shuffle += random.choice(CHAR) 

  return shuffle

with open(LOGFILE, 'a+') as logfile:
  now = time.asctime(time.localtime(time.time()))

  for file_path in sys.argv[1:]:
    # extract file name and dir path from args.
    file_name = file_path.split('/')[-1]
    ext_name = file_name.split('.')[-1]
    dir_path = '/'.join(file_path.split('/')[:-1])
    # construct new names.
    new_name = shuffle()
    before = dir_path+'/'+file_name
    after = dir_path+'/'+new_name+'.'+ext_name
    # renaming process.
    os.rename(before, after)
    logfile.write('{} -:- {} -> {}\n'.format(now, before, after))
