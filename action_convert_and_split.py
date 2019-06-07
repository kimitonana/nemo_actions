#!/usr/bin/env python3

#####################################################################
#####################################################################
## @author: kimitonana
## @description: Nemo Action: 
##   split an album from .cue and .ape files, in .flac format.
##   .cue and .ape must have the same name.
##
##  @dependancies: shntool avconv
##
#####################################################################
#####################################################################

import os
import sys
import subprocess

# extract file and dir names
file_path = sys.argv[1]
dir_path  = '/'.join(file_path.split('/')[:-1])
file_name = file_path.split('/')[-1].split('.')[0]

# build file names for each extension to ease readibility
file_ape  = dir_path+'/'+file_name+'.ape'
file_flac = dir_path+'/'+file_name+'.flac'
file_cue  = dir_path+'/'+file_name+'.cue'

# construct bash commands
avconv = ['avconv', '-i', file_ape, file_flac]
shnsplit = ['shnsplit', '-f', file_cue, '-t', '%n-%t', '-o flac', file_flac, '-d', dir_path]
notify = ['notify-send', '-i', 'python', 'convert_and_split:: '+file_name+' album completed!']

# launch bash commands
if not os.path.isfile(file_cue):
  # sometimes, you might not have the .cue file, only .flac file
  # so we check that out first.
  subprocess.run(avconv)

subprocess.run(shnsplit)
subprocess.run(notify)
