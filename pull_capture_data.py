import os
import subprocess
import fileinput
import time

# processing_foo1s = False
#os.system("adb shell cat /sys/class/power_supply/battery/uevent")

out1 = os.popen("pwd ").read()
print out1
var =70;
f1= "SamCharg-4.1";


output1 = os.popen("adb shell getprop | grep product.brand").read()
output2 = os.popen("adb shell getprop | grep product.model").read()
print output2


output1 = output1.replace("[", "")
output1 = output1.replace("]", "")
output1=output1.split()
print output1[1]

directory = "LOL"
folder = "OLO"

if "samsung" in str(output1[1]).lower():
	print "Samsung S6"
	folder="Samsung S6"
	directory ="/storage/emulated/legacy"
elif "motorola" in str(output1[1]).lower():
	print "Motorola"
	folder="Moto"
	directory ="/storage/emulated/legacy"
elif "google" in str(output1[1]).lower():
	print "nexus found"
	folder = "Nexus"
	directory= "/storage/sdcard0"


pull_command="adb pull "+str(directory)+"/Attribute-data/ '/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+str(folder)+"' "		

print pull_command
os.system(pull_command)
print "completed"