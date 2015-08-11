import os
import subprocess as s
from time import sleep
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


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
#############################################################################
##		Anshal Joshi
## graph plotting for all phones
##
#
# Code Added: added dynamic paths.
#
############################################################################

if "motorola" in brand.lower():

	def read_datafile(file_name):
		data = np.loadtxt(file_name, delimiter=',')
    		return data
	data = read_datafile("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/Attributes-CPU-observation-log.txt")  
	x = [column[0] for column in data]
	y = [abs(column[3]) for column in data]
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	ax1.set_title("")    
	ax1.set_xlabel('Iterations')
	ax1.set_ylabel('Watt')
	ax1.plot(x,y, c='r', label='the data')
	plt.savefig("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/powergraph.jpg")
	plt.show()
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)
	y1 =[column[10] for column in data]
	y2 =[column[11] for column in data]
	y3 =[column[12] for column in data]
	y4 =[column[13] for column in data]
	ax2.set_xlabel('Iterations')
	ax2.set_ylabel('CPU 0 to 4')
	ax2.plot(x,y1, c='r', label='the data')
	ax2.plot(x,y2, c='b', label='the data')
	ax2.plot(x,y3, c='g', label='the data')
	ax2.plot(x,y4, c='y', label='the data')
	plt.savefig("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/CPU.jpg")
	plt.show()
##############################################################################
elif "samsung" in brand.lower():

	def read_datafile(file_name):

		data = np.loadtxt(file_name, delimiter=',')
    		return data

	data = read_datafile("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/Attributes-CPU-observation-log.txt")  
	x = [column[0] for column in data]
	y = [abs(column[3]) for column in data]

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	ax1.set_title("")    
	ax1.set_xlabel('Iterations')
	ax1.set_ylabel('Watt')
	ax1.plot(x,y, c='r', label='the data')
	plt.savefig("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/powergraph.jpg")
	plt.show()
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)
	y1 =[column[10] for column in data]
	y2 =[column[11] for column in data]
	y3 =[column[12] for column in data]
	y4 =[column[13] for column in data]
	ax2.set_xlabel('Iterations')
	ax2.set_ylabel('CPU 0 to 3')
	ax2.plot(x,y1, c='r', label='the data')
	ax2.plot(x,y2, c='b', label='the data')
	ax2.plot(x,y3, c='g', label='the data')
	ax2.plot(x,y4, c='y', label='the data')
	plt.savefig("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/CPUlow.jpg")
	plt.show()
	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111)
	y5 =[column[14] for column in data]
	y6 =[column[15] for column in data]
	y7 =[column[16] for column in data]
	y8 =[column[17] for column in data]
	ax3.set_xlabel('Iterations')
	ax3.set_ylabel('CPU 4 to 7')
	ax3.plot(x,y5, c='r', label='the data')
	ax3.plot(x,y6, c='b', label='the data')
	ax3.plot(x,y7, c='g', label='the data')
	ax3.plot(x,y8, c='y', label='the data')
	plt.savefig("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/CPUhigh.jpg")
	plt.show()
#########################################################################################
elif "google" in brand.lower():
	def read_datafile(file_name):

		data = np.loadtxt(file_name, delimiter=',')
    		return data

	data = read_datafile("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/Attributes-CPU-observation-log.txt")  
	x = [column[0] for column in data]
	y = [column[10] for column in data]

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	ax1.set_title("")    
	ax1.set_xlabel('Iterations')
	ax1.set_ylabel('CPU')
	ax1.plot(x,y, c='r', label='the data')
	plt.savefig("/home/larsip-ubuntu-2/Downloads/data-char/script-data/"+  folder  +"/CPU.jpg")
	plt.show()

	


