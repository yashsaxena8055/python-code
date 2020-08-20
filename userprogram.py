import os
import pyttsx3
import datetime

    
now = datetime.datetime.now()
x=1
pyttsx3.speak("hey their! Im your voice assitant")
print("if you want to close this assistant type QUIT")
while(x==1):
     print (now.strftime("%Y-%m-%d %H:%M:%S"))
     print("what do you want launch",end="  ")
     a = input() 
     if(("don't" in a) or("dont" in a)):
         pyttsx3.speak("ok sir, i will not launch it")
         
         
     elif( ("run" in a) or ("launch" in a) or ( "open" in a)):
         
          if("firefox" in a):
             pyttsx3.speak("launching firefox")
             os.system("firefox")
             os.system("cls")
             os.system("clear")
             
                
          elif("filezilla" in a):
             pyttsx3.speak("launching filezilla") 
             os.system("filezilla")
             os.system("cls")
             os.system("clear")
            
          elif(("gedit" in a) or ("notepad" in a) or ("editor" in a)):
             pyttsx3.speak("launching editor") 
             os.system("gedit")
             os.system("cls")
             os.system("clear")
            
          elif(("bracket" in a) or ("brackets" in a)):
             pyttsx3.speak("launching bracket")  
             os.system("bracket")
             os.system("cls")
             os.system("clear")
                 
          else:
             print("command not available")
             pyttsx3.speak("try again please")
             os.system("cls")
             os.system("clear") 
    
     elif(("exit" in a) or ("quit" in a) or("QUIT" in a) or ("terminate" in a)):
          pyttsx3.speak("pleasure to assist you") 
          break             
    
     else:
          pyttsx3.speak("command not available")   

