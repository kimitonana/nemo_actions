#!/usr/bin/env python3

#####################################################################
#####################################################################
## @author: kimitonana
## @description: Nemo Action: 
##   convert a flac file to mp3 using avconv utility.
##
##  @dependancies: avconv
##
#####################################################################
#####################################################################

import sys
import subprocess

for file_path in sys.argv[1:]:
  file_name = file_path.split('/')[-1].split('.')[0]
  dir_path  = '/'.join(file_path.split('/')[:-1])
  mp3       = dir_path+'/'+file_name+'.mp3'
  flac      = dir_path+'/'+file_name+'.flac'

  # avconv -i "flacfile" -c:a libmp3lame -b:a 320k "mp3file"
  avconv = ['avconv', '-i', flac, '-c:a', 'libmp3lame', '-b:a', '320k', mp3]
  print(avconv)
  subprocess.run(avconv)
