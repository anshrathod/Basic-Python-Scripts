import requests
import decimal
import csv

available_cuisines = ['french', 'italian', 'spanish', 'chinese', 'japanese', 'indian', 'korean', 'american', 'mexican']
# please replace location with the location you preferred
location = 'manhattan'
restaurants = {}

file = open('yelp_data.csv', 'a', encoding='utf-8')
writer = csv.writer(file)
id = []

for cuisine in available_cuisines:
    for offset in range(0, 999, 50):
        params = {
            'term': cuisine,
            'location': location,
            'offset': offset,
            'limit': 50
        }

        headers = {
            # please replace API_key with your API_key obtained from https://www.yelp.com/developers/v3/manage_app
            'Authorization': 'Bearer API_Key'
        }

        response = requests.get(url='https://api.yelp.com/v3/businesses/search', params=params, headers=headers)
        restaurants = response.json()['businesses']
        for restaurant in restaurants:
            if restaurant['id'] not in id:
                id.append(restaurant['id'])
                writer.writerow([restaurant['id'], restaurant['name'], cuisine, ", ".join(restaurant['location']['display_address']),
                                 decimal.Decimal(str(restaurant['coordinates']['latitude'])), decimal.Decimal(str(restaurant['coordinates']['longitude'])),
                                 decimal.Decimal(str(restaurant['rating'])), restaurant['review_count'], restaurant['location']['zip_code']])