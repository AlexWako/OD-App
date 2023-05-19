import shopify
from APIScript import *

def fulfill(path):

    # API information for the store
    api_key = "6ad8ee0c3b4547e27a98d410ea0ad7f8"
    api_secret_key = "c893ad7996cf83741e922034cbf8e3c7"
    private_app_password = ""
    api_version = "2023-04"
    shop_url = f"{api_key}:{private_app_password}@okayamadenim.myshopify.com"

    # Headers for the data being outputted from the requests library
    headers = {
        'X-Shopify-Access-Token': f'{private_app_password}',
        'Content-Type': 'application/json'
    }

    # Connects the store
    session = shopify.Session(shop_url, api_version, private_app_password)

    # Start Session
    shopify.ShopifyResource.activate_session(session)

    # Completes fulfillments done by the given csv file from DHL Express
    info = update_fulfillment(path, headers = headers)

    # Ends session
    shopify.ShopifyResource.clear_session()

    return info
