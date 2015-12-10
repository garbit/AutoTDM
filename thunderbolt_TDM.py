import netifaces
import time
import os


cmd = """
osascript -e 'tell application "System Events" to key code 144 using command down delay'
"""
executed_tdm = False
is_connected = False

polling_delay = 1

debug_mode = False

while True:
	# loop through and output interface data
	for interface in netifaces.interfaces():
		if 'br' in interface:
			# print netifaces.ifaddresses(interface)
			thunderbolt_bridge = netifaces.ifaddresses(interface)
			# if inet addresses have been assigned to the bridge connection, output it
			if 2 in thunderbolt_bridge:
				# let our script know we've connected
				is_connected = True

				if debug_mode == True:
					print 'Thunderbolt connected'

				# check if we have already fired the TDM command
				if executed_tdm == False:
					# execute cmd + F2
					os.system(cmd)
					executed_tdm = True

					print 'Executing TDM mode'

					if debug_mode == True:
						print thunderbolt_bridge[2][0]['broadcast']
			else:

				if debug_mode == True:
					print 'Thunderbold disconnected'
				
				first_connect_event_fired = False
				executed_tdm = False

	time.sleep(polling_delay)