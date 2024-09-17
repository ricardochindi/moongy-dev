import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'demo02'

# Define the table schema
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists
table.wait_until_exists()

# Print the table status
print(f"Table status: {table.table_status}")
