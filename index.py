#!-*-coding:utf-8-*-
import json

def lambda_handler(event, context):
    print(event)

    return {
        "statusCode": 200, 
        "headers": {
            "access-control-allow-headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token ",
            "access-control-allow-methods": "GET,OPTIONS",
            "access-control-allow-origin": "*"
        },
        "body": '{"result":"Hello from Lambda!"}'
    }
