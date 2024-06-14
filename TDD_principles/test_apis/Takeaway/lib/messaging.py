import requests
import logging
import datetime

import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO) # set log level
load_dotenv() # for reading API key from `.env` file.

# Sandbox API URL format: https://api.mailgun.net/v3/sandbox&lt;ID&gt;.mailgun.org/messages
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandboxbef650489a0c405d9de00044d65961e1.mailgun.org/messages"
FROM_EMAIL_ADDRESS = "George <georgegdsmith@hotmail.co.uk>"

class Messaging:
    def __init__(self,request) -> None:
        self.request = request
        self.time = datetime.datetime.now()
        self.subject = f'Your order placed at {self.time.strftime("%H/%M")}'
    
    def create_message(self):
        order_time = self.time + datetime.timedelta(minutes=30)
        return f'Thank you for your order, Your order was placed and will be delivered at {order_time.strftime("%H/%M")}'

    def send_single_email(self,to_address: str):
        try:
            api_key = os.getenv("MAILGUN_API_KEY")# get API-Key from the `.env` file
            resp = self.request.post(MAILGUN_API_URL, auth=(
                "api", api_key),
                data={
                    "from": FROM_EMAIL_ADDRESS,
                    "to": to_address, 
                    "subject": self.subject, 
                    "text": self.create_message()
                    })
            if resp.status_code == 200: # success
                logging.info(f"Successfully sent an email to '{to_address}' via Mailgun API.")
            else: # error
                logging.error(f"Could not send the email, reason: {resp.text}")
        except Exception as ex:
            logging.exception(f"Mailgun error: {ex}")

mess = Messaging(requests)
mess.send_single_email('George <georgegdsmith@hotmail.co.uk>','123 testing','Sending an email via mailgun api')
