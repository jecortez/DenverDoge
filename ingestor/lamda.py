# https://api.petfinder.com/v2/animals?location=colorado&type=dog

import requests
import json
import boto3
import datetime

#to prepend to the filena
def get_filename():
 date = datetime.datetime.now()
 # Fromat is Year_Month_Day_Hour
 string = date.strftime("%Y_%m_%d_%H")
 return string+"_doges.json"

def lambda_handler(event, context):
    # TODO implement
   
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# init list of dogs to put into a list

def get_request_token(): 
	# get token 
    #headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    params = {"grant_type": "client_credentials", "client_id":"hQRiuSSq0RumWHNqDPV8kGfXj80n1cqKvuhNXrDIou0MzeEAOf", "client_secret":"D5PLnW5LUHwYNnfetdVXgEO8pmIEuLLMuwnlyYNk"}
    c = requests.post("https://api.petfinder.com/v2/oauth2/token", data=params)
    return(c.json()['access_token'])

# curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjkwOTFjZTJlNTk1NzgzNmNlOGNhYzJiY2IwMzdjYjgwN2E5ZDFkN2MyYmEzMjMzZWQyNDdlOGY5OGE2YmUzNTgwMGZjNGIyZDc1M2IwM2MwIn0.eyJhdWQiOiJoUVJpdVNTcTBSdW1XSE5xRFBWOGtHZlhqODBuMWNxS3Z1aE5YckRJb3UwTXplRUFPZiIsImp0aSI6IjkwOTFjZTJlNTk1NzgzNmNlOGNhYzJiY2IwMzdjYjgwN2E5ZDFkN2MyYmEzMjMzZWQyNDdlOGY5OGE2YmUzNTgwMGZjNGIyZDc1M2IwM2MwIiwiaWF0IjoxNTcyMTA0NzEwLCJuYmYiOjE1NzIxMDQ3MTAsImV4cCI6MTU3MjEwODMxMCwic3ViIjoiIiwic2NvcGVzIjpbXX0.fR6_7z-XF-CV4pbO6jbuaRKUhLxW-3xLMj_nGU7dUZAlsrtc9BCD0T9G3l3jAMvrk6UY2LIP3tXu5BYeyAWGByFweLOay9rXniwV6pl85Q60BW_EpVP_8VWhy5luY88Y5mVIZb5lOhL1WXLY4jq9vWs2Se2629MrzgNvvT5o1zLKQHbqimghn-60Bsex2lTr4wXIj3WErLhQW4O9cJG4ckRvQ64wagXTKePmVsCtu-AU4OguTPF3L2VOB6eY4qJH_dPotE3pnGjPEUr26s6HqfGAwvJCsQRZCBBRKWH10LwdEz-DSO6UuWvgnZWA_A77WpnoGXOQN9rCZghD8otr4A" GET https://api.petfinder.com/v2/animals



def request_doges_petfinder(petFinderToken):
    list_of_dogs = []
	#if "next_link" in response["meta"]["pagination"]:
    pagenumber=1
    # next_page = "/v2/animals"
    next_link = 'xyz'
    print('abc')
    # loop through pages until they don't exist 
    while next_link:
        print (next_link)
        # next_page= + str(pagenumber)
        #curl -H "Authorization: Bearer" petFinderToken GET https://api.petfinder.com/v2/animals?location=colorado&type=dog
        base_url = "https://api.petfinder.com/v2/animals"

        querystring = {"page":pagenumber,"location":["80003","80004","80010","80011","80012","80013","80014","80016","80020","80021","80022","80026","80027","80031","80033","80035","80046","80104","80108","80109","80110","80113","80120","80121","80123","80123","80123","80125","80126","80127","80130","80134","80138","80162","80204","80205","80207","80209","80210","80211","80212","80215","80220","80221","80222","80223","80227","80227","80228","80231","80234","80239","80246","80250","80299","80301","80302","80304","80305","80401","80401","80403","80433","80437","80439","80454","80474","80501","80503","80601","80621","80640"],"type":"dog","limit":"100"}
        pagenumber= pagenumber + 1

        headers = {
            'location': "colordo",
            'Authorization': "Bearer " + petFinderToken,
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "0922e977-df17-4f33-a31b-3c7ed489b4b9,e1d69704-8217-44a2-b589-4f4b4a6811af",
            'Host': "api.petfinder.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", base_url, headers=headers, params=querystring)
        list_of_dogs+= (response.json()['animals'])
        next_link= ''
        # next_link= response.json()["pagination"]['_links']["next"]
    return list_of_dogs
        # print(response.text)
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

def upload_doge_to_s3(upload_file):
    s3 = boto3.resource('s3')
    s3object = s3.Object('denverdogedata', get_filename())

    s3object.put(
        Body=(bytes(json.dumps(upload_file).encode('UTF-8')))
    )



# def upload_to_s3():
# 	# Create an S3 client
# 	s3 = boto3.client('s3')

# 	filename = 'file.txt'
# 	bucket_name = 'denverdogedata'

# 	# Uploads the given file using a managed uploader, which will split up large
# 	# files automatically and upload parts in parallel.
# 	s3.upload_file(list_of_dogs, bucket_name, key_name)

# get_request_token()
upload_doge_to_s3(request_doges_petfinder(get_request_token()))
