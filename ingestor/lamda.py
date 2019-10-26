# https://api.petfinder.com/v2/animals?location=colorado&type=dog

import requests
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
   
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def get_request_token(): 
	# get token 
    #headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    params = {"grant_type": "client_credentials", "client_id":"hQRiuSSq0RumWHNqDPV8kGfXj80n1cqKvuhNXrDIou0MzeEAOf", "client_secret":"D5PLnW5LUHwYNnfetdVXgEO8pmIEuLLMuwnlyYNk"}
    requests.get("https://api.petfinder.com/v2/oauth2/token", params={params})

# curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjkwOTFjZTJlNTk1NzgzNmNlOGNhYzJiY2IwMzdjYjgwN2E5ZDFkN2MyYmEzMjMzZWQyNDdlOGY5OGE2YmUzNTgwMGZjNGIyZDc1M2IwM2MwIn0.eyJhdWQiOiJoUVJpdVNTcTBSdW1XSE5xRFBWOGtHZlhqODBuMWNxS3Z1aE5YckRJb3UwTXplRUFPZiIsImp0aSI6IjkwOTFjZTJlNTk1NzgzNmNlOGNhYzJiY2IwMzdjYjgwN2E5ZDFkN2MyYmEzMjMzZWQyNDdlOGY5OGE2YmUzNTgwMGZjNGIyZDc1M2IwM2MwIiwiaWF0IjoxNTcyMTA0NzEwLCJuYmYiOjE1NzIxMDQ3MTAsImV4cCI6MTU3MjEwODMxMCwic3ViIjoiIiwic2NvcGVzIjpbXX0.fR6_7z-XF-CV4pbO6jbuaRKUhLxW-3xLMj_nGU7dUZAlsrtc9BCD0T9G3l3jAMvrk6UY2LIP3tXu5BYeyAWGByFweLOay9rXniwV6pl85Q60BW_EpVP_8VWhy5luY88Y5mVIZb5lOhL1WXLY4jq9vWs2Se2629MrzgNvvT5o1zLKQHbqimghn-60Bsex2lTr4wXIj3WErLhQW4O9cJG4ckRvQ64wagXTKePmVsCtu-AU4OguTPF3L2VOB6eY4qJH_dPotE3pnGjPEUr26s6HqfGAwvJCsQRZCBBRKWH10LwdEz-DSO6UuWvgnZWA_A77WpnoGXOQN9rCZghD8otr4A" GET https://api.petfinder.com/v2/animals



def request_doges_petfinder(petFinderToken):
	#if "next_link" in response["meta"]["pagination"]:
    if "_links" in response["pagination"]["next"] is not null:
    	print()
        #curl -H "Authorization: Bearer" petFinderToken GET https://api.petfinder.com/v2/animals?location=colorado&type=dog
    
# def write_to_doge_s3():
       
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


def upload_to_s3():
	# Create an S3 client
	s3 = boto3.client('s3')

	filename = 'file.txt'
	bucket_name = 'denverdogedata'

	# Uploads the given file using a managed uploader, which will split up large
	# files automatically and upload parts in parallel.
	s3.upload_file(filename, bucket_name, key_name)


get_request_token()
