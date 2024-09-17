import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('demo02')

#print(table.creation_date_time)

table.put_item(
   Item={
        'id': "01",
        'first_name': 'Jane2',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
        'category': 'premium'
    }
)
