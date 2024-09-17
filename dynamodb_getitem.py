import boto3
from botocore.exceptions import ClientError

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'demo02'

# Define the primary key for the item you want to retrieve
key = {
    'id': '01'  # Replace with your key attribute and value
}

# Get the table object
table = dynamodb.Table(table_name)

# Function to read an item
def read_item(key):
    try:
        # Read the item from the table
        response = table.get_item(Key=key)

        # Check if the item exists
        if 'Item' in response:
            return response['Item']
        else:
            return None

    except ClientError as e:
        print(f"Error reading item: {e.response['Error']['Message']}")
        return None

# Example usage
item = read_item(key)
if item:
    print("Item found:", item)
else:
    print("Item not found")