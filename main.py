"""
Azure Table Storage Data Importer

This script reads customer data from a JSON file and inserts it into an Azure Table Storage.
It uses the Azure SDK for Python (azure-data-tables) to interact with the Azure Table Storage service.

Requirements:
- Install the Azure SDK for Python: pip install azure-data-tables

The script defines two TypedDict classes (Address and Customer) to represent the structure of customer data.
It also includes functions to parse the JSON file and insert entities into the Azure Table Storage.

Usage:
1. Set the 'file' variable to the path of your customer data JSON file.
2. Set the 'table_name' variable to the name of your Azure Storage Table.
3. Set the 'connection_string' variable to the connection string of Azure Storage account details.

Run the script to insert the customer data into the specified Azure Table.

"""

import json

from azure.data.tables import TableServiceClient, UpdateMode
from typing_extensions import TypedDict

# Specify the JSON file containing customer data
file = "customers.json"
# Define the name of the Azure Storage Table
table_name = 'CustomerTable'
# Define the connection string of the Azure Storage Table
connection_string = "DefaultEndpointsProtocol=https;AccountName=amseproject;AccountKey=VyeWMIJlLo2le9o7HNNcUWMpHAlnKe0LuyPGqKXlvtb9iDUk2I3HSXi9kgBjMeTTLNUH3diPy4jN+AStFjMsug==;EndpointSuffix=core.windows.net"



# Define data structures using TypedDict for better type hinting
class Customer(TypedDict, total=False):
    PartitionKey: str
    RowKey: str
    customerId: str
    firstName: str
    lastName: float
    email: str
    phone: str
    address: str
    dob: str
    ssn: str

    street: str
    city: str
    state: str
    zipCode: str

# Function to parse JSON file and return data
def parse_json_file(file_address):
    with open(file_address, 'r') as json_file:
        data = json.load(json_file)
        return data

# Function to insert into Azure Table Storage
def insert_entities(data):
    with TableServiceClient.from_connection_string(conn_str=connection_string) as table_service_client:
        table_client = table_service_client.get_table_client(table_name)

        for index, row in enumerate(data):
            entity: Customer = {
                "PartitionKey": 'partition1',
                "RowKey": f'row{index}',
                "customerId": row.get('customerId', ''),
                "firstName": row.get('firstName', ''),
                "lastName": row.get('lastName', ''),
                "email": row.get('email', ''),
                "phone": row.get('phone', ''),
                "dob": row.get('dob', ''),
                "ssn": row.get('ssn', ''),
                "street": row.get('address').get('street', ''),
                "city": row.get('address').get('city', ''),
                "state": row.get('address').get('state', ''),
                "zipCode": row.get('address').get('zipCode', '')
            }

            table_client.upsert_entity(entity, mode=UpdateMode.REPLACE)

        # check the inserted data
        my_filter = "PartitionKey eq 'partition1'"
        entities = table_client.query_entities(my_filter)
        for entity in entities:
            print(entity)


if __name__ == "__main__":
    parsed_data = parse_json_file(file)
    if parsed_data is not None:
        insert_entities(parsed_data)
