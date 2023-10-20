import requests
import time
from datetime import datetime, timedelta
from paginate import *

def get_price_rule_codes(headers):
    url = 'https://okayamadenim.myshopify.com/admin/api/2023-04/price_rules.json'
    discounts = []
    while True:
        response = requests.get(
            url = url,
            headers = headers
        )    
        if response.status_code == 200:
            for rule in response.json()['price_rules']:
                discounts.append(rule['id'])
            url = get_next_page(response.headers['link'])
            if url == None:
                break
        else:
            return response.status_code
    return discounts

def update_all_price_rule_collection(headers, price_rule_id_list, collection_id):
    count = 0
    for id in price_rule_id_list:
        url = f'https://okayamadenim.myshopify.com/admin/api/2023-04/price_rules/{id}.json'
        data = {
            'price_rule': {
                'id': id,
                'target_type': 'line_item',
                'target_selection': 'entitled',
                'entitled_collection_ids': [collection_id]
            }
        }
        response = requests.put(
            url = url,
            headers = headers,
            json = data
        )
        print(count, response.status_code)
        count += 1
        time.sleep(0.25)
    return True

def get_new1d_price_rule_codes(headers):
    url = 'https://okayamadenim.myshopify.com/admin/api/2023-04/price_rules.json'
    new_discounts = []
    yesterday_midnight = datetime.combine(datetime.now() - timedelta(days = 1), datetime.min.time()).isoformat()
    midnight = datetime.combine(datetime.now().date(), datetime.min.time())
    while True:
        response = requests.get(
            url = url,
            headers = headers
        )    
        if response.status_code == 200:
            for rule in response.json()['price_rules']:
                if rule['published_at'] > yesterday_midnight and rule['published_at'] < midnight:
                    new_discounts.append(rule['id'])
                else:
                    continue
        else:
            return response.status_code
        break
    return new_discounts
