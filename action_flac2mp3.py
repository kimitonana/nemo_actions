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
  file_name_splitted = file_path.split('/')[-1].split('.')
  if len(file_name_splitted) > 0:
    # if file_name has already '.', concatenate each part with '.'
    # except the last one (which refers to the extension)
    file_name = '.'.join(map(str, file_name_splitted[0:-1]))
  else:
    file_name = file_name_splitted[0]
  dir_path  = '/'.join(file_path.split('/')[:-1])
  mp3       = dir_path+'/'+file_name+'.mp3'
  flac      = dir_path+'/'+file_name+'.flac'

  # avconv -i "flacfile" -c:a libmp3lame -b:a 320k "mp3file"
  avconv = ['ffmpeg', '-i', flac, '-c:a', 'libmp3lame', '-b:a', '320k', mp3]
  print(avconv)
  subprocess.run(avconv)
