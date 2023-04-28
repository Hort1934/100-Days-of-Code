from twilio.rest import Client

TWILIO_SID = "AC899afe95efb241928f6c35a4d6bb9557"
TWILIO_AUTH_TOKEN = "443374229da0cdcf281d6cf5320f1f35"
TWILIO_VIRTUAL_NUMBER = "+16813396341"
TWILIO_VERIFIED_NUMBER = "+380 63 410 9546"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
