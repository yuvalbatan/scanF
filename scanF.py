#!/usr/bin/env python3

import socket
import threading
import ipaddress

def validIP(ipTGT1):
	try:
		ipaddress.ip_address(str(ipTGT1))
		return True
	except:
		return False

# Open a socket and checking if the TCP port is open
# Input - port number to check
# Output - prints open ports
def scnPortsWThreads(port1):
	a_socket = socket.socket()
	a_socket.settimeout(0.5)
	result_of_check = a_socket.connect_ex((ipTGT, port1))
	if result_of_check == 0:
		try:
			serviceName = socket.getservbyport(port1, "TCP");
			print("Open: %d : %s" %(port1, serviceName))
		except:
			print("Open: %d"%port1)
	a_socket.close()

# Append all the ports in the range to rangeLstPorts Array
# Input - 2 ports for range
# Output - Return an array between the ports range
def append2PortLst(port1, port2):
	arr = []
	if port1>port2:
		for i in range(port2, (port1+1)):
			arr.append(i)
	elif port1<port2:
		for i in range(port1, (port2+1)):
			arr.append(i)
	return arr

# Split and check every array for threads
# Input - array to check and run on
# Output - run threads
def arrayCheckAndRun(arr):
	lenArr = len(arr)
	halfArr = int(lenArr/2) #counter
	HalfArrCon = int(lenArr/2) #constant
	startP = 0 #Start point on arr
	for i in arr:
		if startP<HalfArrCon:
			t = threading.Thread(target=scnPortsWThreads, args = (i,))
			t.start()
			startP+=1
		if halfArr<lenArr:
			t2 = threading.Thread(target=scnPortsWThreads, args = (arr[halfArr],))
			t2.start()
			halfArr+=1

# Array of Well Known ports
IMPPorts = [1, 5, 7, 18, 20, 21, 22, 23, 25, 26, 29, 43, 49, 53, 80, 115, 123, 143, 156, 179, 443, 444, 445, 500, 546, 547, 1080, 3389]

try:
	
	print('''
	------------ ------------    ------    ----    ---- ------------ 
	************ ************   ********   *****   **** ************ 
	----         ---           ----------  ------  ---- ----         
	************ ***          ****    **** ************ ************ 
	------------ ---          ------------ ------------ ------------ 
    	       ***** ***          ************ ****  ****** ****         
	------------ ------------ ----    ---- ----   ----- ----         
	************ ************ ****    **** ****    **** ****         

	''')

	ipTGT = input("Welcome To scanF - We Are Scanning TCP Ports With Multi Threading Method For Extra Speed\nWhat Is The Target IP?\n")
	while True:
		valid12 = validIP(ipTGT)
		if valid12 == True:
			break
		ipTGT = input("Please enter valid IP:\n")
		
	options = input("What Option Would You Like?\n-w - Well Known Ports\n-r - Range (Big Range Mean More Time - we recommended max range of 6000 ports)\n-a - All ports\n")
	
	print("-" * 33)
	print("Scanning Target: %s" %(ipTGT))
	print("-" * 33)

	if options=="-w": # Well known ports
		arrayCheckAndRun(IMPPorts)
					
	elif options=="-r": # Range of ports
		lowPort = int(input("Enter Port Number You want to scan From (Lower Port Number):\n"))		
		highPort = int(input("Enter Port Number You want to scan To (Higher Port Number):\n"))
		if lowPort>0 and lowPort<65535 and highPort<= 65535 and highPort>0 and lowPort!=highPort:
			rangeLstPorts = append2PortLst(lowPort, highPort)
			arrayCheckAndRun(rangeLstPorts)
	
	elif options=="-a": # All ports
		arrInArr = []
		sumF = 1
		sumL = 5461
		for i in range(12):
			if i==10:
				arrC = append2PortLst(sumF, sumL)
				arrInArr.append(arrC)
				sumF = sumL+1
				ch = 65535-sumL
				sumL +=ch
			else:
				arrC = append2PortLst(sumF, sumL)
				arrInArr.append(arrC)
				sumF = sumL+1
				sumL +=5461

		for arr in arrInArr:
			arrayCheckAndRun(arr)
		
except:
	print("Something Went Wrong - Please Try Again!")