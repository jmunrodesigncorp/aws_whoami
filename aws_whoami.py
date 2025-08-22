# AWS and low level Python Functions for whoami
# Jason Graham

import json
import boto3
import requests

## aws get whoami information from role
def get_aws_whoami():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    return identity.get('Arn')

### AWS lambda whoami
def lambda_whoami():
    dictoutput = {}
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
            dictoutput["ip_address"] = ip_address
        else:
            print("Could not retrieve public IP address.")
			
    # with lambda api
    datalist = {}
    datalist[host1] = requests.get('http://checkip.amazonaws.com').text.rstrip()
    
	### output something to test basic
    string = json.dumps(datalist, indent=4)

    #get all output to json format
    dictoutput["aws_whoami"] = get_aws_whoami()
    string = json.dumps(dictoutput, indent=4)
    return string

def lambda_handler(event, context):
    # output the whoami info in json
    output = lambda_whoami()
    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }








