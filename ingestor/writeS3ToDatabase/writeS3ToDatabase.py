import boto3
import json
import datetime
from datetime import datetime, timedelta
import smart_open
import pymysql.cursors
import uuid
from smart_open import open
import time

def get_photos(photos_list):
	if photos_list:
		return photos_list[0]['full']
	else:
		return ""

def get_filename():
	 date = datetime.now() - timedelta(hours=6)
	 # Format is Year_Month_Day_Hour
	 string = date.strftime("%Y_%m_%d_%H")
	 return "petfinder/"+string+"_doges.json"

def lambda_handler(event, context):
	# TODO implement
	grab_file_from_s3()
	return {
		'statusCode': 200,
		'body': json.dumps('Uploaded!')
	}

def get_activity_level(json_object):
	return "LOW"
	
def write_to_database(json_object):
	
	connection = pymysql.connect(host='denverdoge.co5hqpwgtu5w.us-east-1.rds.amazonaws.com',
							 user='root',
							 password='denverdoge',
							 db='denverdoge',
							 charset='utf8mb4',
							 port=3306)

	batch_id = str(uuid.uuid1())
	with connection.cursor() as cursor:
		# Create a new record
		# sql = """
		# INSERT INTO `pets` (`source_id`, `batch_id`, `external_id`, `url`, `type`, `species`, `age`, `gender`, `size`, `coat`, `tags`, `name`, `description`, `image_url`, `status`, `breeds_primary`, `breeds_secondary`, `breeds_mixed`, `colors_primary`, `colors_secondary`, `colors_tertiary`, `attributes_activity_level`, `attributes_spayed_neutered`, `attributes_house_trained`, `attributes_declawed`, `attributes_special_needs`, `attributes_shots_current`, `environment_children`, `environment_dogs`, `environment_cats`)
		# VALUES
		# (1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)	
		# sql = """
		# INSERT INTO `pets` (`source_id`, `batch_id`, `external_id`, `url`, `type`, `species`, `age`, `gender`, `size`, `coat`, `tags`, `name`, `description`, `image_url`, `status`, `breeds_primary`, `breeds_secondary`, `breeds_mixed`, `colors_primary`, `colors_secondary`, `colors_tertiary`, `attributes_activity_level`, `attributes_spayed_neutered`, `attributes_house_trained`, `attributes_declawed`, `attributes_special_needs`, `attributes_shots_current`, `environment_children`, `environment_dogs`, `environment_cats`)
		# VALUES
		# (1, "batch_id", "external_id", "url", "type", "species", "age", "gender", "size", "coat", "tags", "name", "description", "image_url", "status", "breeds_primary", "breeds_secondary", 1, "colors_primary", "colors_secondary", "colors_tertiary", "attributes_activity_level", 1, 1, 1, 1, 1, 1, 1, 1)	
		# """

		# cursor.execute(sql, ())
		# connection.commit()
		check_dupe_sql = """
			SELECT *
			FROM `pets`
			WHERE external_id = %s
		"""
		
		cursor.execute(check_dupe_sql, (json_object['id']))
		result=cursor.fetchone()
		if result:
			print("ID " + str(json_object['id']) + " is a duplicate! Not adding.")
		else:

			sql = """
			INSERT INTO `pets` (`source_id`, `batch_id`, `external_id`, `url`, `type`, `species`, `age`, `gender`, `size`, `coat`, `tags`, `name`, `description`, `image_url`, `status`, `breeds_primary`, `breeds_secondary`, `breeds_mixed`, `colors_primary`, `colors_secondary`, `colors_tertiary`, `attributes_activity_level`, `attributes_spayed_neutered`, `attributes_house_trained`, `attributes_declawed`, `attributes_special_needs`, `attributes_shots_current`, `environment_children`, `environment_dogs`, `environment_cats`)
			VALUES
			(1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %r, %s, %s, %s, %s, %r, %r, %r, %r, %r, %r, %r, %r)	
			"""
			cursor.execute(sql, (
				batch_id,
				str(json_object['id']),
				str(json_object['url']),
				str(json_object['type']),
				str(json_object['species']),
				str(json_object['age']),
				str(json_object['gender']),
				str(json_object['size']),
				str(json_object['coat']),
				str(json_object['tags']),
				str(json_object['name']),
				str(json_object['description']),
				get_photos(json_object['photos']),
				str(json_object['status']),
				str(json_object['breeds']['primary']),
				str(json_object['breeds']['secondary']),
				bool(json_object['breeds']['mixed']),
				str(json_object['colors']['primary']),
				str(json_object['colors']['secondary']),
				str(json_object['colors']['tertiary']),
				get_activity_level(str(json_object)),
				bool(json_object['attributes']['spayed_neutered']),
				bool(json_object['attributes']['house_trained']),
				bool(json_object['attributes']['declawed']),
				bool(json_object['attributes']['special_needs']),
				bool(json_object['attributes']['shots_current']),
				bool(json_object['environment']['children']),
				bool(json_object['environment']['dogs']),
				bool(json_object['environment']['cats'])
				))
			connection.commit()
			print("Added " + str(json_object['id']) + " to the database")

sample_data = """[
  {
    "_links": {
      "organization": {
        "href": "/v2/organizations/co125"
      },
      "self": {
        "href": "/v2/animals/46392785"
      },
      "type": {
        "href": "/v2/types/dog"
      }
    },
    "age": "Adult",
    "attributes": {
      "declawed": null,
      "house_trained": false,
      "shots_current": false,
      "spayed_neutered": true,
      "special_needs": false
    },
    "breeds": {
      "mixed": false,
      "primary": "Pit Bull Terrier",
      "secondary": null,
      "unknown": false
    },
    "coat": null,
    "colors": {
      "primary": null,
      "secondary": null,
      "tertiary": null
    },
    "contact": {
      "address": {
        "address1": "610 Abbott Lane",
        "address2": null,
        "city": "Colorado Springs",
        "country": "US",
        "postcode": "80905",
        "state": "CO"
      },
      "email": null,
      "phone": "719-473-1741"
    },
    "description": null,
    "distance": 73.2301,
    "environment": {
      "cats": null,
      "children": null,
      "dogs": null
    },
    "gender": "Female",
    "id": 46392785,
    "name": "MARGIE",
    "organization_id": "CO125",
    "photos": [
      {
        "full": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392785/1/?bust=1572117883",
        "large": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392785/1/?bust=1572117883&width=600",
        "medium": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392785/1/?bust=1572117883&width=300",
        "small": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392785/1/?bust=1572117883&width=100"
      }
    ],
    "published_at": "2019-10-26T19:19:41+0000",
    "size": "Large",
    "species": "Dog",
    "status": "adoptable",
    "status_changed_at": "2019-10-26T19:19:41+0000",
    "tags": [],
    "type": "Dog",
    "url": "https://www.petfinder.com/dog/margie-46392785/co/colorado-springs/humane-society-of-the-pikes-peak-region-co125/?referrer_id=b868674b-58e2-471e-ab1f-110592706191"
  },
  {
    "_links": {
      "organization": {
        "href": "/v2/organizations/co27"
      },
      "self": {
        "href": "/v2/animals/46392767"
      },
      "type": {
        "href": "/v2/types/dog"
      }
    },
    "age": "Adult",
    "attributes": {
      "declawed": null,
      "house_trained": false,
      "shots_current": false,
      "spayed_neutered": false,
      "special_needs": false
    },
    "breeds": {
      "mixed": false,
      "primary": "American Staffordshire Terrier",
      "secondary": null,
      "unknown": false
    },
    "coat": null,
    "colors": {
      "primary": null,
      "secondary": null,
      "tertiary": null
    },
    "contact": {
      "address": {
        "address1": "10705 Fulton St",
        "address2": null,
        "city": "Brighton",
        "country": "US",
        "postcode": "80601",
        "state": "CO"
      },
      "email": null,
      "phone": "(303) 288-3294"
    },
    "description": "Meet Harley! *May be vocal in his kennel but he is great once out and about! *Kennel trained *Knows basic...",
    "distance": 5.7381,
    "environment": {
      "cats": null,
      "children": null,
      "dogs": null
    },
    "gender": "Male",
    "id": 46392767,
    "name": "HARLEY",
    "organization_id": "CO27",
    "photos": [
      {
        "full": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392767/1/?bust=1572117877",
        "large": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392767/1/?bust=1572117877&width=600",
        "medium": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392767/1/?bust=1572117877&width=300",
        "small": "https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/46392767/1/?bust=1572117877&width=100"
      }
    ],
    "published_at": "2019-10-26T19:19:30+0000",
    "size": "Medium",
    "species": "Dog",
    "status": "adoptable",
    "status_changed_at": "2019-10-26T19:19:30+0000",
    "tags": [],
    "type": "Dog",
    "url": "https://www.petfinder.com/dog/harley-46392767/co/brighton/adams-county-animal-shelter-adoption-center-co27/?referrer_id=b868674b-58e2-471e-ab1f-110592706191"
  }
]
"""
def grab_file_from_s3():
	# Create an S3 client
	# s3 = boto3.client('s3')

	# filename = date_string + '_doges.jsonl'
	# bucket_name = 'denverdogedata'

	# Uploads the given file using a managed uploader, which will split up large
	# files automatically and upload parts in parallel.

	print("Grabbing file")
	file_contents = ""
	for line in open('https://denverdogedata.s3-us-west-1.amazonaws.com/' + str(get_filename())):
		file_contents += line

	for json_object in json.loads(file_contents):
		write_to_database(json_object)
	#json.read(sample_data)
