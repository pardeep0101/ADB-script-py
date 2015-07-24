import os
import subprocess as s
from time import sleep

out1 = os.popen("pwd ").read()
print out1

 
 ########################################################
 ##
 ##	Max R. Berrios 
 ##
 
 # reduce the amount of un handle process to 0 
 # and use less shell like struct that an be turn 
 # against us later . 

## Code Added: Pardeep:
## added the default value and exception just to avoid getting error if phone is not connected 
output3 = "undefined"
try:
	output3 = s.check_output(['adb' , 'shell' , 'getprop'])
except s.CalledProcessError as e:
	brand = "NA"
	model = "NA"
	print "exception occured"


for i in output3.split("\n"):
	if not ":" in i:
 		continue
 	tmp = i.strip("\r[]").split(":")
 	opt = tmp[0].strip().strip("[]")
 	resp = tmp[1].strip().strip("[]")
 	
 	if "product.brand" in opt:
 		brand = resp
 	elif "product.model" in opt:
 		model = resp
 ##
 ##
 ########################################################
 
if "samsung" in brand.lower():
	print "Samsung S6"
	folder="Samsung S6"
	directory ="/storage/emulated/legacy"
elif "motorola" in brand.lower():
	print "Motorola"
	folder="Moto"
	directory ="/storage/emulated/legacy"
elif "google" in brand.lower():
	print "Nexus found"
	folder = "Nexus"
	directory= "/storage/sdcard0"
else:
	print "ADB is down"

# Code added: Pardeep
# added the condition to run the pull command only when phone is connected.
if not "undefined" in output3:
	pull_command="adb pull "+  directory  +"/Attribute-data/ '/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"' "		
	# print pull_command
	os.system(pull_command)
print "completed"
