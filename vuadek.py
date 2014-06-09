print("vUADEk")


import os
import subprocess

#mport json

zm_input = "spacedeb.suk"
zm_output = "test.wav"
zm_mp3 = "test.mp3"
zm_home = os.path.expanduser("~")
zm_pth_workdir = zm_home+"/.vuadek/"

if not os.path.exists(zm_pth_workdir):
    os.makedirs(zm_pth_workdir)
zm_fl_remains = zm_pth_workdir+"remains"


scan_result = subprocess.Popen(["uade123", "--scan", zm_home+"/Dokumenty"],stdout=subprocess.PIPE)

with open(zm_fl_remains, 'w') as f:
	for line in scan_result.stdout:
		f.write(line.decode('utf-8'))		
f.closed

with open(zm_fl_remains, 'r') as f:
	zm_input = [line.rstrip('\n') for line in f]
	for item in zm_input:
		subprocess.call(["uade123", "--detect-format-by-content", "-f",zm_output, "--filter=A1200", "--normalise", "--speed-hack", "-v", "--headphones", item])
		print(item)
f.closed




#call(["lame", "--verbose", "--preset", "standard", zm_output, zm_mp3])
#call(["rm", zm_output])

