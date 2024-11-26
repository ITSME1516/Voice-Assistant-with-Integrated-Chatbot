#modules used for the program
import datetime
import pyttsx3 
import speech_recognition as sr
import pywhatkit as p
import pandas as pd
import pyjokes
import wikipedia
import pyautogui as pa
import chatbot as ct
#some constant variables
i=0
command=''
name="selfie"
#contacts are imported
contacts=pd.read_csv("contact.csv")
contact=contacts.set_index("name")

#fort talking out
engine = pyttsx3.init() 
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

#to recognise the voice
listener=sr.Recognizer()

#to avoid writing the same code again and again for speekout and lisening
def talk(out):
    engine.say(out)
    engine.runAndWait()
"""def lisen():
    global command
    with sr.Microphone() as source:
        print('leasining..')
        speech=listener.listen(source)
        command=listener.recognize_google(speech).lower()
        print(command)
"""

def command():
    global command
    command = input("Enter Comand")
    return command

#greatings
def greating():
    while True:
        tm=datetime.datetime.now()
        hour=tm.strftime('%H')
        if 6<int(hour)<12:
            out="Good Morning"
            talk(out)
            break
        elif 15>int(hour)>=12:
            out="Good Afternoon"
            talk(out)
            break
        elif 19>=int(hour)>=15:
            out="Good Evening"
            talk(out)
            break
        else:
            out="Good Night"
            talk(out)
            break


def main():
    global name
    global command
    try:
        
        #talk('how can i help you?')        
        command()
        #lisen()
        
        #calling selife to find she is there or not
        if  command=="selfie":
            j=0
            while j==0:
                try:
                    out="Yes!,How can i help you?"
                    talk(out)
                    command()
                    #lisen()
                    j=1
                except Exception as e:
                    j=0

                  
        
        elif  "video" in command:
            j=0
            while j==0:
                try:
                    print("which vedio or song you what to watch?")
                    talk("which vedio or song you what to watch?")
                    command()
                    #lisen()
                    if command=='nothing'  :
                        break

                    out="Playing "+command+" song"
                    talk(out)
                    p.playonyt(command)
                    j=1
                    global i
                    i=1
                except Exception as e:
                    j=0
                

                    
        
        elif  "time"  in command:
            time=datetime.datetime.now().strftime('%I %M %p')
            out="current time is "+ time
            talk(out)

            
        
        elif  "search" in command:
            j=0
            while j==0:
                try:
                  out='What you want to search..'
                  talk(out)
                  command()
                  #lisen()
                  if command=='nothing'  :
                        break
                  p.search(command)  
                  j=1
                except Exception as e:
                    j=0

                    
        #saying to stop the conversation
        elif "stop"  in command:
            print(command)
            i=1
            talk("Bhai Bhai")

        #send whatsapp message     
        elif  "whatsapp message" in command:
            j=0
            while j==0:
                try:
                    print("whom you what to send the message..?")
                    talk("whom you what to send the message..?")
                    command()
                    #lisen()
                    
                    for k in contact.loc[command]:
                        k=str(k)
                        number="+91"+k
                        print(number)
                        out="what message you what to send :"
                        talk(out)
                        command()
                        #lisen()
                        msg=command
                        p.sendwhatmsg_instantly(number, msg)
                        out="msg sent successfully.."
                        talk(out)
                        j=1
                        pa.hotkey("Alt","F4")
                except Exception as e:
                    talk("please say again")
                    j=0

        elif "spam message"  in command:
                j=0
                while j==0:
                    try:
                        print("whom you what to send the message..?")
                        talk("whom you what to send the message..?")
                        command()
                        #lisen()
                        for k in contact.loc[contact]:
                            k=str(k)
                            number="+91"+k
                            print(number)
                        out="what message you what to send :"
                        talk(out)
                        command()
                        #lisen()
                        msg=command
                        talk("How many messages you want to send ")
                        command()
                        #lisen()
                        how_many=int(command)
                        p.sendwhatmsg_instantly(number, msg)
                        for no_msg in range(how_many):
                            pa.typewrite(msg)
                            pa.press("enter")
                        out="spam msg sent successfully.."
                        talk(out)
                        j=1
                        pa.hotkey("Alt","F4")
                    except Exception as e:
                        talk("please say again.")
    
        #asking selfie to read and display something from wikipedia
        elif "wikipedia"   in command:
            j=0
            while j==0:
                try:
                    print("About whom you what to know..?")
                    talk("About whom you what to know..?")
                    command()
                    #lisen()
                    if command=='nothing'  :
                        break
                    info=wikipedia.summary(command,5)
                    print(info)
                    talk(info)         
                    j=1
                except Exception as e:
                    talk("please say again")
                    j=0
        elif "shutdown" in command:
            try:
                talk("confirm your command yes or no")
                command()
                #lisen()
                command=command.lower()
                if command=='yes':
                    p.shutdown()
                else:
                    talk("canceling shutdown process")
            except Exception as e:
                talk("confirm your command.press yes or no")
                confirm=input("confirm your command,(Y/N):")
                confirm=confirm.lower()
                if command=="y":
                    talk("shutdown process started")
                    p.shutdown()
                else:
                    talk("canceling shutdown process")
        else:
            talk(ct.get_res(command))
        
    #if any disturbance occure 
    except Exception as e:
        pass
        #talk("sorry!")



greating()

# main function

while i==0:
    main()
"""
while True:
    command()command = 
    #lisen()
    if "selfie" in command:
        i=0
    elif i==0:
        main()
"""