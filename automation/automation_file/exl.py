import getpass
import telnetlib

# Declare variables for storing IP address
IP = "localhost"
# Declare variables to store username
user = input("Enter your username :")
# Use getpass module to get the password from the user
password = getpass.getpass()
# Pass the IP address variable in to the telnet which is imported
telnet = telnetlib.Telnet(IP)
telnet.read_until(b"Username : ")
# Use ascii code to send data to cisco switches
telnet.write(user.encode("ascii") + b"\n")
if password:
    telnet.read_until(b"Password: ")
    telnet.write(password.encode("ascii") + b"\n")
telnet.write(b"enable  \n")
telnet.write(b"cisco  \n")
telnet.write(b"conf t  \n")
telnet.write(b"hostname CoreSW  \n")
telnet.write(b"end  \n")
telnet.write(b"exit  \n")
print(telnet.read_all().decode("ascii"))

#device list file
cisco_ios = {'device_type':'cisco_ios_ssh', 'ip': '10.10.10.27', 'username': 'admin', 'password': 'passwd', 'port': 22,}
cisco_xr ={'device_type': 'cisco_xr_ssh', 'ip': '10.10.10.27', 'username': 'admin', 'pasword': 'passwd', 'secret': '', 'port': 9722,}
arista_veos = {'device_type':'arista_eos_ssh', 'username': 'admin', 'password':'passwd', 'secret': '', 'port': 8622,}


# network code

from datetime import datetime
from netmiko import ConnectHandler
from my_devices import cisco_ios, cisco_xr, arista_veos


def main():
    device_list = [cisco_ios, cisco_xr, arista_veos]
    start_time = datetime.now()
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        print("{}: {}".format(net_connect.device_type, net_connect.find_prompt()))
    print("Time elapsed:  {}\n".format(datetime.now()))
    if check_bgp(net_connect):
        print("BGP currently configured")
    else:
        print("No BGP")
        print("Time elapse: {}\n".format(datetime.now() - start_time))

if __name__ == "__main__":
    main()

