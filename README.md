# rain-notification
Sends a Whatsapp notification if there's raining for today. It uses Twilio to send the messages and gets the meteorological information from http://www.aemet.es.

In order to use this program, you must schedule it everyday and change the internal parameters to fit your criteria. The majority of these parameters (Twilio tokens, Whatsapp numbers...) are gotten with env variables.

My idea is to host this in Heroku and schedule it everyday at 05:00.
