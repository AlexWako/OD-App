import shopify
from APIScript import *

def fulfill(path):

    # API information for the store
    api_key = "d01c57ce8d6a90dcac5aaaaa8d60cf46"
    api_secret_key = "6bfa86392f9df3bd00a8a37e1675aa99"
    private_app_password = "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"
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
