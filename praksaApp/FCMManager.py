import firebase_admin
from firebase_admin import credentials, messaging
from rest_framework.decorators import api_view
from rest_framework.response import Response

cred = credentials.Certificate("praksaApp/Utils/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

@api_view(['POST'])
def sendPush(request):
    message = messaging.Message(
        notification = messaging.Notification(
            title = request.data["title"],
            body = request.data["msg"],
        ),
        token = request.data["registration_token"],
    )
    
    
    response = messaging.send(message)
    return Response(response)

def send(msg, title, tokens):
    message = messaging.Message(
        notification = messaging.Notification(
            title = title,
            body = msg,
        ),
        token = tokens,
    )
    
    
    response = messaging.send(message)
    return Response(response)
    