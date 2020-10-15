import boto3
import requests
import datetime
import time
import cv2

#Credentials----------------------------------------------------------------------------------
client = boto3.client('rekognition',
                      aws_access_key_id="ASIAQWBSEWH2DAK3GI4J",
                      aws_secret_access_key="JKS3ZrLLZY9VSn6+2L7VS41H0M6qCUe85kUM9Cz7",
                      aws_session_token="FwoGZXIvYXdzEK7//////////wEaDFPuDcJEZJY3SttnRyLHAd6JGd70kRKAc1AzujrWj2Mb2jwOfJFTlENlZuuRzw7V6sUu30nDRDshg2F11s4Z9iuKleczShATcAdD++xBG8hcbv3Q+d2Z/TiJ/tkm4velNH4lV+4y8b0L11sr/5Y43n7U99f1D0RDrn8HjpBW0DYDr3kvkCDIPOr0P0aR5hEm65QprBz1paLcE4yxYJ1k9RerA49oZ3LTo3GKe9LEX9MRRH+5JZMGQ39Kf7SIUHoCNdnxUQEqfnloJ2hvT1OECZJGxvqNnYAoqPug/AUyLTRBFpTwesbhJR0E6Wsp6FvrKiCNGyNl++QECyBr43bz0fXExsFN3k4/1KCnbQ==",
                      region_name='us-east-1')

#Capture images for every 1 hour and store the image with current date and time -----------------------------------------------------------------------------------
for j in range(0, 6):
    current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
    print(current_time)
    camera = cv2.VideoCapture(0)
    for i in range(20):
        return_value, image = camera.read()
        if (i == 19):
            cv2.imwrite('C:/Users/Ratan kumar singh/Desktop/Images/Elon_Musk_Royal_Society.jpg', image)
    del (camera)

#Send the captured image to AWS S3 Bucket--------------------------------------------------------------------------------------
    clients3 = boto3.client('s3', region_name='us-east-1')
    clients3.upload_file("C:/Users/Ratan kumar singh/Desktop/Images/Elon_Musk_Royal_Society.jpg", 'custom-labels-console-us-east-1-ab317384a8', current_time+'.jpg')

    #Recoginze students in captured image ---------------------------------------------------------------------------------------
    with open(r'C:/Users/Ratan kumar singh/Desktop/Images/Elon_Musk_Royal_Society.jpg','rb') as source_image:
        source_bytes = source_image.read()
    print(type(source_bytes))

    print("Recognition Service")
    response = client.detect_custom_labels(
        ProjectVersionArn='arn:aws:rekognition:us-east-1:047349805556:project/AI-Powered_Hourly_Attendance_Capturing_System/version/AI-Powered_Hourly_Attendance_Capturing_System.2020-10-09T13.53.09/1602231493042',

        Image={
            'Bytes': source_bytes
        },

    )

    print(response)
    if not len(response['CustomLabels']):
         print('Not identified')

    else:
        str = response['CustomLabels'][0]['Name']
        print(str)
        # Update the attendance of recognized student in DynamoDB by calling the API
        url = "https://c5vjdzmfti.execute-api.us-east-1.amazonaws.com/test_sample?name=" + str
        resp = requests.get(url)
        print(resp)
        if resp.status_code==200:
            print("Success")

    time.sleep(3600)
