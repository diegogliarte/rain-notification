from twilio.rest import Client
import os

def send_whatsapp(message, sender, receiver):
    """
    Sends a message with the Twilio API. It needs 2 environment variables called TWILIO_ACCOUNT_SID and
    TWILIO_AUTH_TOKEN. The "sender" and "receiver" numbers should include the prefix with the "+" sign
    :param message: message that will be send
    :param sender: twilio phone from the message will be send
    :param receiver: personal phone where the message will be send
    :return: do not return nothing
    """

    ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
    AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:' + sender.replace(" ", "")
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:' + receiver.replace(" ", "")

    client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)

if __name__ == "__main__":
    message = "Hello! This is a message test"
    sender = "+PXXXXXXXXX"
    receiver = "+PPYYYYYYYYY"
    send_whatsapp(message, sender, receiver)