# AWS and low level Python Functions for whoami
# Jason Graham

import json
import adder
import boto3
import botocore
import requests


		
### AWS lambda whoami
def lambda_whoami():

    # normal python, no aws:
    try:
        # Using a service that returns the public IP address in plain text
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None

    if __name__ == "__main__":
        ip_address = get_public_ip_address()
        if ip_address:
            return ip_address
        else:
            print("Could not retrieve public IP address.")
			
	# with lambda api
	# return requests.get('http://checkip.amazonaws.com').text.rstrip()
	
### output something to screen to test

# adder output
string = json.dumps(datalist, indent=4)
print(string)



