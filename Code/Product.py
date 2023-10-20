import requests
from datetime import datetime, timedelta
from paginate import *

def get_product_in_collection(headers, collection_id):
    url = f'https://okayamadenim.myshopify.com/admin/api/2023-04/collections/{collection_id}/products.json'
    products = []
    while True:
        response = requests.get(
            url = url,
            headers = headers
        )    
        if response.status_code == 200:
            for product in response.json()['products']:
                products.append(product['id'])
            url = get_next_page(response.headers['link'])
            if url == None:
                break
        else:
            return response.status_code
    return products

def get_new1d_products(headers):
    url = "https://okayamadenim.myshopify.com/admin/api/2023-04/products.json?selectedView=active&status=ACTIVE&order=created_at%20desc"
    new_products = []
    yesterday_midnight = datetime.combine(datetime.now() - timedelta(days = 1), datetime.min.time()).isoformat()
    midnight = datetime.combine(datetime.now().date(), datetime.min.time())
    while True:
        response = requests.get(
            url = url,
            headers = headers
        )
        if response.status_code == 200:
            for product in response.json()['products']:
                if product['published_at'] > yesterday_midnight and product['published_at'] < midnight:
                    new_products.append(product['id'])
                else:
                    continue
        else:
            return response.status_code
        break
    return new_products
