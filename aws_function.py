
import getpass
import threading
import boto3
import subprocess
from gtts import gTTS
import playsound
import datetime
import pync
import os
import pip
from googletrans import Translator
import speech_recognition as sr
from sys import platform
from plyer import notification
from sys import platform


r = sr.Recognizer()  # Voice Recognition

path = "/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Linux/Python_Voice_Automation/"



def detect_os():
    if platform == "linux" or platform == "linux2":
        return 'clear'
    elif platform == "darwin":
        return 'clear'
    elif platform == "win32":
        return 'cls'
      

def speak(text):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save("voice.mp3")
    playsound.playsound('voice.mp3', True)
    
   
clear_cmd = detect_os()

def listen():
    try:
        with sr.Microphone() as source:
            voice = r.listen(source)
            speak('We are Processing your request ...')
        if voice:
            command = r.recognize_google(voice)
            command = command.lower()
            return command
        else:
            speak("Sorry Sir I won't get you, Please Try Again")
    except Exception as e:
        listen()
        
        
def aws_config():
    count = 0
    if count == 0:
        print("\033[33m Please wait while downloading the dependency !")
        pip.main(['install', 'boto3'])
        import boto3
        ec2 = boto3.client('ec2')
        s3 = boto3.client('s3')
        count += 1
    os.system(clear_cmd)
    print()
    print()
    print('''\033[97m
       `.---::-.   `:::`-:/:` .-::.      .---.
      `.---.-::/:  `/++++oooo/ossss+   :syyyyys/   +ssssooo+  `-///:.    ... `..`                           \033[92m Select your choice:\033[97m
      ``..   -://` .+++/.-oooo/:+sss- .syy/-:yyy/  /ooosssso `ossoooo+`  /+/://::-                      \033[92m--------------------------------\033[97m
        `..--:://` .+++-  /ooo  .sss-  .--``.syy+     -ssso` /sso  :oo+  +++/.-:::`
      `.---..-://` .+++.  /ooo  .sss-  :oyyyyyyy+    /yyy+   sss/  `ooo. +++.  :::.                     \033[94m 1. \033[93m Installing Amazon CLI\033[97m
      .---   -://` .+++.  /ooo  .sss- :yyy:``syy+  `+yyy:    sss/   ooo- ++/.  -::`                     \033[94m 2. \033[93m List All AvailabilityZone !\033[97m
      .---``.:://- .+++.  /ooo  .sss- +yyy  .yyyo `oyyys+/-` +ss+  `ooo. ++/.  -::`                     \033[94m 3. \033[93m Configuring AWS CLI Tools\033[97m
      `.----:--:/- .+++.  /ooo  .sss- :yyyssyyyyy:.yyyyyysss`.sss:-/oo/  ++/.  -::`                     \033[94m 4. \033[93m List All Instances \033[97m
        ````   .`   .--`  .::-  `///`  -+ooo:`/o: `+:..`.-/+` .+soooo:`  ///`  -:-` \033[33m                    \033[94m 5. \033[93m Launch an Instance\033[33m
                 /+:`                             ./osyyso. *                                           \033[94m 6. \033[93m List All KeyPairs \033[33m
                  `/so/-`                         `-.-.-sh:                                             \033[94m 7. \033[93m Attach A Volume\033[33m
                    `:oyys+:-`                  `-/oyy/ yy`                                             \033[94m 8. \033[93m List All SecurityGroups\033[33m
                       ./oyyyyyso++//:::://++oyhhhho:` /y-                                              \033[94m 9. \033[93m Create S3 Bucket\033[33m
                          `-/+syyyyhhhhhhhhhhhyo/-`    +.                                               \033[94m 10. \033[93mList All Subnets\033[33m
                                `--://///::-.                                                           \033[94m 11. \033[93mAttach S3 bucket to CloudFront\033[33m
    		   	                                                                                \033[94m 12. \033[93mList All InstanceTypeOfferings!\033[33m
    			                                                                                \033[94m 13. \033[93mTerminate os\033[33m
    			                                                                                \033[94m 14. \033[93mList All Volume Created\033[33m
    			                                                                                \033[94m 15. \033[93mList All VolumeOffering\033[33m
                                                                                                        \033[94m 16. \033[93mExit\033[33m
    \033[0m''')
    speak('Welcome To Amazon Web Services, , Here is the List of tasks which we can do for you')
    speak('Tell me, What do you want to do')
