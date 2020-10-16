# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:37:33 2020

@author: Lalitha
"""

import boto3
import requests

client=boto3.client('rekognition',
                    aws_access_key_id="ASIAQWBSEWH2P3AHRWHH",
                        aws_secret_access_key="L2G8CTZ8jhRbGf5SdM7bUbIjeHxZvqtym4c9xpQC",
                    aws_session_token="FwoGZXIvYXdzEMP//////////wEaDFdZAiVMG1OYoOPNXyLHAeuDE3vi/TaDdCkPXsEO/WaQZBYTLAEwGJBdV3sjD98jenkSTyiUrzu4m6kF6x5zyly40AnEY1IdDGw+30xx2hBPzg7jfw01lrK5udOQmTAU+w2u5c6+uPLlFeRSnI/MLjNIklVLw5p8g4Ox1cLYuWACcqWCIUrbKSkjrThbzupnPU0UHKAn41a+pietzLllIig4JaVz8ws0GIdPBo4WkqbcXI5jQRM9q8TRmTJdOKp/i2K4IuOPcVkqpekJjIVB55bThEj042Io4tSl/AUyLYhynLogbStAV85WKl1PzmArzZ+OwtWpwOutP78t1FwmM/3vK8wFkrOs8CFRTA==",

                    region_name='us-east-1')

with open(r'C:/Users/Ratan kumar singh/Desktop/Images/mark-zuckerberg.jpg', 'rb') as source_image:
    source_bytes=source_image.read()
print(type(source_bytes))

print("Recognition Service")
response = client.detect_custom_labels(
    ProjectVersionArn='arn:aws:rekognition:us-east-1:047349805556:project/AI-Powered_Hourly_Attendance_Capturing_System/version/AI-Powered_Hourly_Attendance_Capturing_System.2020-10-09T13.53.09/1602231493042',
   
    Image={
        'Bytes':source_bytes

    },
   
)

print(response)
if not len(response['CustomLabels']):
    print('Student not identified')

else:
    str_1=response['CustomLabels'][0]['Name']
    print(str_1)
    url=" https://c5vjdzmfti.execute-api.us-east-1.amazonaws.com/test_sample?name="+str_1
    print(url)
    resp = requests.get(url)
    print(resp)
