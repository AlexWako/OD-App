import shopify
import pandas as pd
import requests
from TextEdit import *
from Response import *
from PyToHTML import *

# Creates a dictionary of the order information off the csv file
def get_order(csv_file):

    # Seperates the csv files into different parts of necessary data
    csv = pd.read_csv(csv_file)
    order = list(csv.iloc[:, 1])
    track = list(csv.iloc[:, 16])
    email = list(csv.iloc[:, 23])
    name = list(csv.iloc[:, 0])

    return (order, track, email, name)

# Creates and posts a fulfillment
def create_fulfillment(order_num, track_num, remaining, headers):

    # Get the order related to the order_num
    order = shopify.Order.find_first(name = f"#{order_num}")

    # Get the fulfillment data of the order
    fulfillment_order = shopify.FulfillmentOrders.find_first(order_id = order.id)

    data = {
        'fulfillment': {
            'tracking_info': {
                'number': track_num,
                'company': 'DHL Express',
            },
            'notify_customer': True,
            'line_items_by_fulfillment_order': [
                {
                'fulfillment_order_id': fulfillment_order.id
                }
            ]
        }
    }

    response = requests.post(
        'https://okayamadenim.myshopify.com/admin/api/2023-04/fulfillments.json',
        headers = headers,
        json = data
    )

    # If there is an error, add it to a dictionary containing orders that need to be fulfilled manually
    if response.status_code not in (200, 201, 202, 422):
        remaining["Order Number"].append(order_num)
        remaining["Tracking Number"].append(track_num)
        remaining["Response Status"].append(response.status_code)

# Update fulfillment order
def update_fulfillment(csv_file, headers):

    # Split the csv file into different columns
    info = get_order(csv_file)

    order_nums = info[0]
    track_nums = info[1]
    emails = info[2]
    names = info[3]

    remaining = {
        "Order Number": [],
        "Tracking Number": [],
        "Response Status": []
        }

    # Go through each order in the csv file
    for num in order_nums:

        # Get the tracking number related to the order
        track_num = track_nums[order_nums.index(num)]

        # Get the email related to the order
        email = emails[order_nums.index(num)]

        # Get the last name related to the order
        name = names[order_nums.index(num)]
        split_name = name.split(" ")
        last_name = split_name[-1]

        # Self explanatory function
        num = remove_space(str(num)).upper()

        # For an order without any features (most common version)
        if num.isnumeric():

            create_fulfillment(num, track_num, remaining, headers)

        # If the shippment has multiple orders
        elif "+" in num:

            # Creates a list of the orders
            nums = num.split("+")

            for num in nums:

                # If one of the order number is an exchange
                if "E" in num:

                    # Get the email template for exchanges
                    body = exchange_render(last_name, track_num)

                    # Send the email
                    exchange(email, body)

                else:

                    create_fulfillment(num, track_num, remaining, headers)

        # If the order is an exchange
        elif "E" in num:

            # Get the email template for exchanges
            body = exchange_render(last_name, track_num)

            # Send the email
            exchange(email, body)

        elif "P" in num:

            # Add the order to remaining
            remaining["Order Number"].append(num)
            remaining["Tracking Number"].append(track_num)
            remaining["Response Status"].append("Partial Fulfillment")

    if remaining["Order Number"] == []:
        return "Fulfillments are complete"
    else:
       return pd.DataFrame(remaining)
