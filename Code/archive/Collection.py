import requests

def create_collection(headers, title, product_ids):

    json_data = {
        'custom_collection': {
            'title': title,
            'collects': product_ids,
        },
    }

    response = requests.post(
        f'https://okayamadenim.myshopify.com/admin/api/2023-04/custom_collections.json',
        headers = headers,
        json = json_data,
    )

    return response.status_code

def update_collection(headers, collection_id, product_ids):

    json_data = {
        'custom_collection': {
            'id': collection_id,
            'collects': product_ids,
        },
    }

    response = requests.put(
        f'https://okayamadenim.myshopify.com/admin/api/2023-04/custom_collections/{collection_id}.json',
        headers = headers,
        json = json_data,
    )

    return response.status_code