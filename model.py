import requests

baseUrl = 'https://health.gov/myhealthfinder/api/v3'

def get_content(string):
	string = string[:string.find('</p>')]
	string = string.replace("<p>", '')
	string = string.replace("<span>", '')
	string = string.replace("</span>", '')
	string = string.replace("&nbsp;", '')
	return string

def get_topics(keyword):
	response = requests.get(f"{baseUrl}/topicsearch.json?lang=en&keyword={keyword}")
	# print("Topics Response Status: " + str(response.status_code))

	try:
		result = response.json()
		resources = result["Result"]["Resources"]["Resource"]
	except KeyError:
		return False
	
	topicsList = {}
	for resource in resources:
		title = resource['Title']
		topicsList[title] = {
			'url': resource["AccessibleVersion"],
			'image': resource['ImageUrl'],
			'image_alt': resource['ImageAlt'],
			'more_info_title': 'The Basics: Overview',
			'more_info_content': get_content(resource["Sections"]["section"][0]['Content'])
		}

	return topicsList

def get_categories():
	response = requests.get(f"{baseUrl}/itemlist.json")
	result = response.json()
	items = result["Result"]["Items"]["Item"]
	itemList = []
	for item in items:	
		if item["Type"] == "Category":
			itemList.append(item["Title"])
	return itemList


itemList = get_categories()