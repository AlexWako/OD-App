from ScanForFile import *
from TextEdit import *
import requests 
import re

url = 'https://okayamadenim.myshopify.com/admin/api/2023-04/customers?segment_query=customer_added_date%20%3E%3D%20-1d%20'

unique_phone = set({})
repeat_phone = {}
no_phone = set({})

while True:

    headers = {
        'X-Shopify-Access-Token': "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",
        'Content-Type': 'application/json',
    }

    response = requests.get(
        url = url,
        headers = headers
    )    

    if response.status_code == 200:

        length = len(unique_phone)
        for customer in response.json()['customers']:
            try:
                if customer['default_address'] != []:
                    if customer['default_address']['phone'] != None or customer['default_address']['phone'] != "":
                        unique_phone.add(get_int(customer['default_address']['phone']))
                        if len(unique_phone) == length:
                            try:
                                repeat_phone[get_int(customer['default_address']['phone'])].append(customer['default_address']['first_name'] + ' ' + customer['default_address']['last_name'])
                            except:
                                repeat_phone[get_int(customer['default_address']['phone'])] = [customer['default_address']['first_name'] + ' ' + customer['default_address']['last_name']]
                    else:
                        try:
                            no_phone.add(customer['default_address']['first_name'] + ' ' + customer['default_address']['last_name'])
                        except:
                            no_phone.add(customer['email'])
            except:
                no_phone.add(customer["email"])
                
        matches = re.findall(r'<([^>]+)>; rel="([^"]+)"', response.headers['link'])
        for match in matches:
            if 'next' in match:
                url = match[0]
            else:
                continue
                
    else:

        break

with open('CustomerAddress.txt', 'a') as file:
    for phone in unique_phone:
        if type(phone) != str:
            file.write("None\n")
        else:
            file.write(phone + "\n")
    file.close()

with open('RepeatPhone.txt', 'a') as file:
    for key, value in repeat_phone.items():
        file.write(key + " : " + ", ".join(value) + "\n")
    file.close()

with open('NoPhone.txt', 'a') as file:
    for data in no_phone:
        if data == None:
            file.write("None\n")
        else:
            file.write(data + "\n")
    file.close()