import speech_recognition as sr
import paho.mqtt.client as mqtt
import time

# AWS IoT Core settings
iot_endpoint = "Your IoT Endpoint"
topic = "Your Topic"

# Certificate filenames
cert_file = ".pem.crt"
key_file = ".pem.key"
root_ca_file = "AmazonRootCA1.pem"  # Download from AWS

# Initialize the MQTT client
client = mqtt.Client(client_id="VoiceToText-Device1")
client.tls_set(certfile=cert_file, keyfile=key_file, ca_certs=root_ca_file)


# Connect to AWS IoT Core
client.connect(iot_endpoint, port=8883)

# Initialize the SpeechRecognition recognizer
recognizer = sr.Recognizer()

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT Core with result code " + str(rc))

# Set the on_connect callback
client.on_connect = on_connect

# Start the MQTT loop
client.loop_start()

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print("You said: " + text)
        client.publish(topic, text)  # Publish text to MQTT topic
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the API.")
    
    time.sleep(1)  # Add a delay to avoid flooding MQTT messages

# Disconnect the MQTT client gracefully on exit
client.disconnect()
