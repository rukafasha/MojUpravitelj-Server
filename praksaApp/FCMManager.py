# from firebase_admin import messaging
# import firebase_admin
# from firebase_admin import credentials

# Initialize the Firebase Admin SDK
# cred = credentials.Certificate('C:\Users\User\Desktop\MojUpravitelj-Server\praksaApp\Utils\serviceAccountKey.json')
# firebase_admin.initialize_app(cred)



# Construct the message payload
# message = messaging.Message(
#     notification=messaging.Notification(
#         title='Notification Title',
#         body='Notification Body'
#     ),
#     token='device-token'
# )

# # Send the message to the device
# response = messaging.send(message)

import firebase_admin
from firebase_admin import credentials, messaging
from rest_framework.decorators import api_view
from rest_framework.response import Response

cred = credentials.Certificate("praksaApp/Utils/serviceAccountKey.json")
print(cred)
firebase_admin.initialize_app(cred)

@api_view(['POST'])
# def sendPush(title, msg, registration_token, dataObject=None):
def sendPush(request):
    print("ndc dcnj")
    message = messaging.Message(
        notification = messaging.Notification(
            title = request.data["title"],
            body = request.data["msg"],
        ),
        # data = request.data["dataObject"],
        token = request.data["registration_token"],
    )
    
    
    response = messaging.send(message)
    print("Successfully sent message: ", response)

    return Response(response)
    