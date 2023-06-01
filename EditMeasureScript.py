import requests
import re
from bs4 import BeautifulSoup

#　Get product data from typed product name
def get_product(product, headers):

    product = product.replace('"', "'")

    query = '''
        query($productName: String!) {
            products(query: $productName, first: 1) {
                edges {
                    node {
                        id
                        descriptionHtml
                    }
                }
            }
        }
    '''

    variables = {
        'productName': product
    }

    data = {
        'query': query,
        'variables': variables
    }


    response = requests.post(
        "https://okayamadenim.myshopify.com/admin/api/2023-04/graphql.json",
        json = data,
        headers = headers
    ).json()

    # If the product does not exist return None
    if response['data']['products']['edges'] == []:
        return False

    # Returns the product ID and the HTML body
    return (re.search(r'\d+', response['data']['products']['edges'][0]['node']['id']).group(), response['data']['products']['edges'][0]['node']['descriptionHtml'])

# Get the description of the body
def get_table(html_body):

    # Return the table part of the description
    soup = BeautifulSoup(html_body, 'html.parser')
    return soup.find_all('table')

# Get original sizing of the object
def get_og_cm_data(html_body):

    # Creates a new dictionary for the measurements and types of data being queried
    measure_row = []

    # Seperate the html table into a list of rows
    cm_rows = get_table(html_body)[0].find_all('tr')

    # Iterates through the strings of html code in the table
    for row in cm_rows:

        cells = row.find_all('td')

        # Extract the content of each row
        data = [cell.get_text(strip=True) for cell in cells]

        # Add the data into the measure_row if
        if cm_rows.index(row) != 0:

            measure_row.append(data)

        else:

            measurements = data

    return (measurements, measure_row)

def edit_table(og_html, table_cm_data):

    soup = BeautifulSoup(og_html, 'html.parser')

    tables = soup.find_all('table')

    new_tables = tables

    for table in new_tables:
        rows = table.find_all('tr')
        if "CM" in str(rows):
            for i, row in enumerate(rows):
                cells = row.find_all('td')
                if i != 0:
                    for j, cell in enumerate(cells):
                        if j != 0:
                            cell.clear()
                            cell.append(str(table_cm_data[i - 1][j - 1]))
        elif "Inches" in str(rows):
            for i, row in enumerate(rows):
                cells = row.find_all('td')
                if i != 0:
                    for j, cell in enumerate(cells):
                        if j != 0:
                            cell.clear()
                            cell.append(str(round((float(table_cm_data[i - 1][j - 1])/2.54), 1)))

    for table, new_table in zip(tables, new_tables):

        table.replace_with(new_table)

    return str(soup)

def update_measure_table(product_id, html_code, headers):
    data = {
        'product': {
            'id': int(product_id),
            'body_html': html_code
        }
    }

    response = requests.put(
        f"https://okayamadenim.myshopify.com/admin/api/2023-04/products/{product_id}.json",
        json = data,
        headers = headers
    )

    # Check the response
    if response.status_code == 200:
        return "Complete"
