#!/usr/bin/python3.4

import sys
import os
import subprocess

zm_home = os.path.expanduser("~")
zm_pth_workdir = zm_home+"/.vuadek/"

if not os.path.exists(zm_pth_workdir):
    os.makedirs(zm_pth_workdir)
zm_fl_remains = zm_pth_workdir+"remains"

pathname = os.path.dirname(sys.argv[1])

if not os.path.isfile(zm_fl_remains):
	print('nie istnieje')
	scan_result = subprocess.Popen(["uade123", "--scan", os.path.abspath(pathname)],stdout=subprocess.PIPE)
	with open(zm_fl_remains, 'w') as f:
		for line in scan_result.stdout:
			f.write(line.decode('utf-8'))		
	f.closed

print('istnieje')
with open(zm_fl_remains, 'r') as f:
	zm_input = [line.rstrip('\n') for line in f]
	for item in zm_input:
		head, tail = os.path.split(item)
		subprocess.call(["uade123", "--detect-format-by-content", "-f",zm_pth_workdir+tail+'.wav', "--filter=A1200", "--normalise", "--speed-hack", "-v", "--headphones", item])
		subprocess.call(["lame", "--verbose", "--preset", "standard", zm_pth_workdir+tail+'.wav', head+'/'+tail+'.mp3'])
		subprocess.call(["rm", zm_pth_workdir+tail+'.wav'])
f.closed




#call(["lame", "--verbose", "--preset", "standard", zm_output, zm_mp3])
#call(["rm", zm_output])

