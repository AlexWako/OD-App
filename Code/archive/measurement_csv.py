import requests
import shopify
import pandas as pd
from ShopifyApp import *
from paginate import *
from EditMeasureScript import *

headers = {
    'X-Shopify-Access-Token': # API Secret Key,
    'Content-Type': 'application/json',
}

html_body = []
product_id = []

response = requests.get(
    url = 'https://okayamadenim.myshopify.com/admin/api/2023-07/collections/5215072/products.json',
    headers = headers
)

while get_next_page(str(response.headers)):

    for data in response.json()['products']:
        html_body.append(data['body_html'])
        product_id.append(data['id'])
    
    response = requests.get(
        url = get_next_page(str(response.headers)),
        headers = headers
    )

for html in response.json()['products']:
    html_body.append(html['body_html'])
    product_id.append(data['id'])

measurements = []

for i, body in enumerate(html_body):
    try:
        data = get_og_cm_data(body)
        measurements.append([[product_id[i]], data[1]])
    except:
        continue

data_list = []

for data in measurements:
    id = data[0]
    measure = data[1]
    if len(measure) == 2:
        data_list.append({'id': id, 'Type 1': measure[0], 'Type 2': measure[1]})
    else:
        data_list.append({'id': id, 'Type 1': measure, 'Type 2': None})

df = pd.DataFrame(data_list)

df.to_csv('measurements.csv')
