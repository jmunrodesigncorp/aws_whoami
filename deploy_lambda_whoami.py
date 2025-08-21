## deploys lambda whoami after testing independently
import aws_whoami

#create the handler
def lambda_handler(event, context):

   # whoami output
   ipaddr = lambda_whoami()
   
   return {
        'statusCode': 200,
        'body': json.dumps(ipaddr)
   }