import json

from azure.data.tables import TableServiceClient, UpdateMode
from typing_extensions import TypedDict

file = "customers.json"
table_name = 'CustomerTable'
connection_string = "DefaultEndpointsProtocol=https;AccountName=amseproject;AccountKey=VyeWMIJlLo2le9o7HNNcUWMpHAlnKe0LuyPGqKXlvtb9iDUk2I3HSXi9kgBjMeTTLNUH3diPy4jN+AStFjMsug==;EndpointSuffix=core.windows.net"


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


def parse_json_file(file_address):
    with open(file_address, 'r') as json_file:
        data = json.load(json_file)
        return data


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
