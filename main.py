import whatsapp
import rain
import os
from time import sleep

def main():
    print("Beginning rain-notification.")
    stats = rain.get_rain("http://www.aemet.es/xml/municipios_h/localidad_h_25120.xml")
    messages = []
    for key, value in stats.items():
        if value[0].count("lluvia") or int(value[1]) >= 40:
            messages.append(f"Around {key}:00h, there's a {value[1]}% of raining. The description is '{value[0]}.'")
            
            
    sender = os.environ["TWILIO_SENDER"]
    receiver = os.environ["TWILIO_RECEIVER"]
    receiver2 = os.environ["TWILIO_RECEIVER2"]
    for message in messages:
        whatsapp.send_whatsapp(message, sender, receiver)
        whatsapp.send_whatsapp(message, sender, receiver2)
        sleep(1)
if __name__ == "__main__":
    main()


