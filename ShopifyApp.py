import shopify

 # API information for the store
api_key =
api_secret_key =
private_app_password =
api_version = "2023-04"
shop_url = f"{api_key}:{private_app_password}@okayamadenim.myshopify.com"

# Headers for the data being outputted from the requests library
headers = {
    'X-Shopify-Access-Token': private_app_password,
    'Content-Type': 'application/json'
}

def activate_session():

    # Connects the store
    session = shopify.Session(shop_url, api_version, private_app_password)

    # Start Session
    shopify.ShopifyResource.activate_session(session)

def close_session():

    # Ends session
    shopify.ShopifyResource.clear_session()

