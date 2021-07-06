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
