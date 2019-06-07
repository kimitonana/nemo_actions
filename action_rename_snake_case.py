#!/usr/bin/env python3

#####################################################################
#####################################################################
## @author: kimitonana
## @description: Nemo Action: 
##   rename file or directory by using snake_case naming conventions
##
##   JoJo no Kimyou na Bouken - Ougon no Kaze - 32
##   -->
##   jojo_no_kimyou_na_bouken_-_ougon_no_kaze_-_32
##
#####################################################################
#####################################################################

import os
import sys
import time

LOGFILE = '/tmp/snake_case_renaming.log'

with open(LOGFILE, 'a+') as logfile:
  now = time.asctime(time.localtime(time.time()))

  for file_path in sys.argv[1:]:
    # extract file name and dir path from args.
    file_name = file_path.split('/')[-1]
    dir_path = '/'.join(file_path.split('/')[:-1])
    # construct new names.
    new_name = file_name.lower().replace(' ', '_')
    before, after = dir_path+'/'+file_name, dir_path+'/'+new_name
    # renaming process.
    os.rename(before, after)
    logfile.write('{} -:- {} -> {}\n'.format(now, before, after))
