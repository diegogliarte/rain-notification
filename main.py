import whatsapp
import rain
import os

def main():
    stats = rain.get_rain("http://www.aemet.es/xml/municipios_h/localidad_h_25120.xml")
    messages = []
    for key, value in stats.items():
        if value[0].count("lluvia") or int(value[1]) >= 15:
            messages.append(f"Around {key}:00, there's a {value[1]}% of raining. The description is '{value[0]}.'")

    sender = os.environ["TWILIO_SENDER"]
    receiver = os.environ["TWILIO_RECEIVER"]

    for message in messages:
        whatsapp.send_whatsapp(message, sender, receiver)

if __name__ == "__main__":
    main()


