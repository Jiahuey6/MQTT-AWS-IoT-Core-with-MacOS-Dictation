
# MQTT-AWS-IoT-Core-with-MacOS-Dictation
Use MacOS Dictation to parse text to AWS IoT Core with MQTT




## Screenshots

![](https://cdn.discordapp.com/attachments/1137013235720134707/1145725442238714007/Animation.gif)


## Prerequisites 
1. MacOS with Dictation Enabled <sub> (Press fn twice to activate) </sub>
1. An AWS Account with an IoT Core Thing
1. IoT_endpoint <sub> (get from IoT Core Settings) </sub> Example: **xxxxxxxxxxx-xxx.iot.us-east-1.amazonaws.com**
1. A cert_file and a private key_file (Get from creating a "Thing")

## Installation

Install python, speech_recognition, paho-mqtt, pyaudio

```bash
  brew install python
  pip3 install SpeechRecognition paho-mqtt pyaudio

```

### Setup Instructions
1. Install requisites
1. Put py file in a folder along with all the certificate files
1. Modify the py file variables (Put your values with double quotes in between " ") 
```
iot_endpoint = " " - get from IoT Core Settings on the left panel
topic = " " - thing topic
cert_file = " " - file ending in crt
key_file = " " - private key file
```
4. Ready to launch. Open your Iot Core service and Click on "MQTT test client" on the left panel. On the "Subscribe to a topic", fill in the topic you have named from creating a "Things" matching **topic= "Your Topic"** and click on **Subscribe**
5. On your Mac, open a terminal and point to the folder containing the python script example: `% cd Desktop/Python`
6. Execute the script with 
```
python3 speak.py
```
7. When the console returns `Connected to AWS IoT Core with result code 0` followed by `Listening...` , **press** fn twice activate the Dictation Feature on the terminal and begin speaking to the mic.
8. After speaking, press on **"Done"** and the voice should be recorded and sent to aws Subscriptions at the bottom matching the topic.
+ The Dictation feature **may not work** on other 3rd party terminals, it is recommended to use the Terminal by Apple and verify the Dictation is working on other application (Spotlight).


### Instructions for Creating IoT Core and Certificates
1. Go to AWS IoT Core and select Manage > All Devices > Things on the left panel
1. Click on "Create Things"
1. Check on Create Single Thing and click Next
1. Give the "Thing" a name, leave all options on default and click Next
1. On the Device certificate screen, check on "Auto-generate a new certificate (recommended)" and proceed to Next.

1. On the Policies screen, attatch a policy. If none is listed click on "Create policy" and refer to the bottom section.
1. After attaching a policy, click on "Create thing"
1. Download (You will not be able to download most of these files again)
```
+ Device Certificate
+ Public key file
+ Private key file
+ RSA 2048 bit key: Amazon Root CA 1
```
9. Click on "Done"



### Create policy
1. Give the policy a name
1. On the Policy Document tab, select <sup>*</sup> (All IoT Core actions) in the "Policy action" selection box
1. Provide ARN in "Policy resource" (ARN can be generated in IAM Service)
1. Click Done
