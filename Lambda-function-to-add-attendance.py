import json
import boto3

dynamo= boto3.resource('dynamodb')
table = dynamo.Table('student_attendance')

def lambda_handler(event, context):
    resp = table.get_item(Key={"name":event['name']})
    # print(resp['Item'])
    if resp['Item'].get('count'):
        count = resp['Item']['count']
    else:
        count = 0
    count= count+1
    inp = {"name":event['name'],"count":count}
    table.put_item(Item=inp)
    # TODO implement
    return "successful"