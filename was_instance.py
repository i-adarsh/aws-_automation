import boto3
import subprocess
from gtts import gTTS
import playsound
import pync
import speech_recognition as sr
from sys import platform
from plyer import notification

client = boto3.client('ec2', region_name='us-west-2')

amazon = "ami-0915bcb5fa77e4892"
redhat = "ami-096fda3c22c1c990a"
windows = "ami-02642c139a9dfb378"

win_sg = "sg-0b22b456f7d71d9a5"
amazon_sg = "sg-08586f9c84fed2afb"
red_sg = "sg-09891af7ebd11747f"

key = 'iAdarsh'

# cmd = f"aws ec2 run-instances  --image-id ami-0947d2ba12ee1ff75 --instance-type t2.micro  --count 1 --subnet-id subnet-be09bfd8 --security-group-ids  sg-0584862d272fe0bae --key-name iAdarsh"

count = "1"


def speak(text):
    tts = gTTS(text=text, lang='hi')
    tts.save("voice.mp3")
    playsound.playsound('voice.mp3', True)


def instances_type(vm):
    if 'windows' in vm:
        cmd = f"aws ec2 run-instances  --image-id {windows} --instance-type t2.micro  --count {count} --subnet-id subnet-be09bfd8 --security-group-ids  {win_sg} --key-name {key}"
        print(subprocess.getoutput(cmd))
        speak("instances launched Successfully")
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            pync.notify('instances launched Successfully', title='Adarsh - Automation')
        elif platform == "win32":
            notification.notify(title="Adarsh - Automation",
                                message='instances launched Successfully',
                                app_icon=None,
                                timeout=10,
                                toast=False)
    elif 'amazon' in vm or "amazon linux" in vm:
        cmd = f"aws ec2 run-instances  --image-id {amazon} --instance-type t2.micro  --count {count} --subnet-id subnet-be09bfd8 --security-group-ids  {amazon_sg} --key-name {key}"
        print(subprocess.getoutput(cmd))
        speak("instances launched Successfully")
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            pync.notify('instances launched Successfully', title='Adarsh - Automation')
        elif platform == "win32":
            notification.notify(title="Adarsh - Automation",
                                message='instances launched Successfully',
                                app_icon=None,
                                timeout=10,
                                toast=False)
    elif 'red' in vm or 'hat' in vm or "redhat" in vm or "redhat linux" in vm:
        cmd = f"aws ec2 run-instances  --image-id {redhat} --instance-type t2.micro  --count {count} --subnet-id subnet-be09bfd8 --security-group-ids  {red_sg} --key-name {key}"
        print(subprocess.getoutput(cmd))
        speak("instances launched Successfully")
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            pync.notify('instances launched Successfully', title='Adarsh - Automation')
        elif platform == "win32":
            notification.notify(title="Adarsh - Automation",
                                message='instances launched Successfully',
                                app_icon=None,
                                timeout=10,
                                toast=False)


r = sr.Recognizer()  # Voice Recognition
while True:
    with sr.Microphone() as source:
        speak('What can I do for you?')
        voice = r.listen(source)
        speak('We are Processing your request ...')
    if voice:
        command = r.recognize_google(voice)
        command = command.lower()
    else:
        continue
    if 'launch' in command or 'ec2' in command or 'os' in command or 'instances' in command or 'instance' in command or 'operating system' in command:
        speak('Which type of Operating System you want ?')
        with sr.Microphone() as source:
            voice = r.listen(source)
            speak('We are Processing your request ...')
        if voice:
            command = r.recognize_google(voice)
            command = command.lower()
            instances_type(command)
        else:
            continue
    else:
        speak("Sorry Sir I won't get you, Please Try Again")
