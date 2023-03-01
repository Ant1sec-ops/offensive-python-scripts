
 
import uuid
print("[*] Welcome to mac extractor [*]")
print("[*] Usage: python3 macExtractor.py [*]")
# printing the value of unique MAC
# address using uuid and getnode() function
print("")
my_mac = hex(uuid.getnode())
print ("Your mac address is: ", my_mac)
