import json
import urllib.request

def lambda_handler(event, context):
    # Make a request to cat-facts
    req = urllib.request.Request("https://cat-fact.herokuapp.com/facts/random")

    """
    The response looks like:
    {
        "used": false,
        "source": "user",
        "type": "cat",
        "deleted": false,
        "_id": "58e007db0aac31001185ecf7",
        "user": "58e007480aac31001185ecef",
        "text": "There are cats who have survived falls from over 32 stories (320 meters) onto concrete.",
        "__v": 0,
        "updatedAt": "2019-08-24T20:20:02.145Z",
        "createdAt": "2018-03-02T21:20:02.322Z"
    }
    """
    # This `json.load()` function takes that {} object and creates a python dictionary (kind of) from it
    response_json = json.load(urllib.request.urlopen(req))
    
    # We extract the "text" field from that dictionary
    fact = response_json['text']
    
    # And return it here!
    return {
        # 2xx status codes mean "successes" in Web codes.
        # 2xx = success, 3xx = redirects (something moved), 4xx means you (client) messed something up, 5xx means server messed something up
        # I have no idea what 1xx responses are for ("continue"), I think it had to do with when the internet was super slow
        'statusCode': 200,
        'body': fact
    }
