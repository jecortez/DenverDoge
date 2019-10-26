import boto3
import json
import datetime
import smart_open
import pymysql.cursors
import uuid


def lambda_handler(event, context):
	# TODO implement
	return {
		'statusCode': 200,
		'body': json.dumps('Hello from Lambda!')
	}
def get_activity_level(json_object):
	return "LOW"
def write_to_database(json_object):
	json_object = json.loads(json_object)
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
		sql = """
		INSERT INTO `pets` (`source_id`, `batch_id`, `external_id`, `url`, `type`, `species`, `age`, `gender`, `size`, `coat`, `tags`, `name`, `description`, `image_url`, `status`, `breeds_primary`, `breeds_secondary`, `breeds_mixed`, `colors_primary`, `colors_secondary`, `colors_tertiary`, `attributes_activity_level`, `attributes_spayed_neutered`, `attributes_house_trained`, `attributes_declawed`, `attributes_special_needs`, `attributes_shots_current`, `environment_children`, `environment_dogs`, `environment_cats`)
		VALUES
		(1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %r, %s, %s, %s, %s, %r, %r, %r, %r, %r, %r, %r, %r)	
		"""
		cursor.execute(sql, (
			batch_id,
			json_object['id'],
			json_object['url'],
			json_object['type'],
			json_object['species'],
			json_object['age'],
			json_object['gender'],
			json_object['size'],
			json_object['coat'],
			str(json_object['tags']),
			json_object['name'],
			json_object['description'],
			json_object['photos'][0]['full'],
			json_object['status'],
			json_object['breeds']['primary'],
			json_object['breeds']['secondary'],
			json_object['breeds']['mixed'],
			json_object['colors']['primary'],
			json_object['colors']['secondary'],
			json_object['colors']['tertiary'],
			get_activity_level(json_object),
			json_object['attributes']['spayed_neutered'],
			json_object['attributes']['house_trained'],
			json_object['attributes']['declawed'],
			json_object['attributes']['special_needs'],
			json_object['attributes']['shots_current'],
			json_object['environment']['children'],
			json_object['environment']['dogs'],
			json_object['environment']['cats']
			))
		connection.commit()


sample_data = """{
			"id": 124,
			"organization_id": "NJ333",
			"url": "https://www.petfinder.com/cat/nebula-124/nj/jersey-city/nj333-petfinder-test-account/?referrer_id=d7e3700b-2e07-11e9-b3f3-0800275f82b1",
			"type": "Cat",
			"species": "Cat",
			"breeds": {
				"primary": "American Shorthair",
				"secondary": null,
				"mixed": false,
				"unknown": false
			},
			"colors": {
				"primary": "Tortoiseshell",
				"secondary": null,
				"tertiary": null
			},
			"age": "Young",
			"gender": "Female",
			"size": "Medium",
			"coat": "Short",
			"name": "Nebula",
			"description": "Nebula is a shorthaired, shy cat. She is very affectionate once she warms up to you.",
			"photos": [
				{
					"small": "https://photos.petfinder.com/photos/pets/124/1/?bust=1546042081&width=100",
					"medium": "https://photos.petfinder.com/photos/pets/124/1/?bust=1546042081&width=300",
					"large": "https://photos.petfinder.com/photos/pets/124/1/?bust=1546042081&width=600",
					"full": "https://photos.petfinder.com/photos/pets/124/1/?bust=1546042081"
				}
			],
			"status": "adoptable",
			"attributes": {
				"spayed_neutered": true,
				"house_trained": true,
				"declawed": false,
				"special_needs": false,
				"shots_current": true
			},
			"environment": {
				"children": false,
				"dogs": true,
				"cats": true
			},
			"tags": [
				"Cute",
				"Intelligent",
				"Playful",
				"Happy",
				"Affectionate"
			],
			"contact": {
				"email": "petfindertechsupport@gmail.com",
				"phone": "555-555-5555",
				"address": {
					"address1": null,
					"address2": null,
					"city": "Jersey City",
					"state": "NJ",
					"postcode": "07097",
					"country": "US"
				}
			},
			"published_at": "2018-09-04T14:49:09+0000",
			"distance": 0.4095,
			"_links": {
				"self": {
					"href": "/v2/animals/124"
				},
				"type": {
					"href": "/v2/types/cat"
				},
				"organization": {
					"href": "/v2/organizations/nj333"
				}
			}
		}
"""
def grab_file_from_s3(date_string):
	# Create an S3 client
	# s3 = boto3.client('s3')

	# filename = date_string + '_doges.jsonl'
	# bucket_name = 'denverdogedata'

	# # Uploads the given file using a managed uploader, which will split up large
	# # files automatically and upload parts in parallel.
	# s3.download_file(filename, bucket_name, key_name)
	# print(s3)
	# with open(filename, 'wb') as f:
	#     s3.download_fileobj(bucket_name, 'OBJECT_NAME', f)
	#for line in smart_open.smart_open('https://denverdogedata.s3-us-west-1.amazonaws.com/petfinder+doges/colorado-animals.csv'):
	#	pet = json.load(line)
	#json.read(sample_data)
	print()

grab_file_from_s3("")
write_to_database(sample_data)