import requests
import argparse
import json
print("[*] Usage: python3 geoLocationTracker.py -i facebook.com")
print("")
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--ipaddress", help="IP address to track")
	args = parser.parse_args()
	ip = args.ipaddress
	url = "http://ip-api.com/json/"+ip
	response = requests.get(url)
	data = json.loads(response.content)
	print("[*] Initial output! [*]")
	print(data)
	print("")
	print("[*] Clean output! [*]")
	print("\t[+] IP\t\t\t", data["query"])
	print("\t[+] CITY\t\t", data["city"])
	print("\t[+] ISP\t\t\t", data["isp"])
	print("\t[+] LOCATION\t\t", data["country"])
	print("\t[+] REG\t\t\t", data["regionName"])
	print("\t[+] TIME\t\t", data["timezone"])
	print("\t[+] ZIP\t\t\t", data["zip"])
	print("\t[+] LAT\t\t\t", data["lat"])
	print("\t[+] LON\t\t\t", data["lon"])
	
