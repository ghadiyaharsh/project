import pyttsx3

if __name__ == '__main__':  '''start main program from here  
meaning of this line is that if this file is run as main program then only run the following code'''

print("welcome to RoboSpeaker")
print("enter the text you want to convert into voice")
x=input("Enter the text you want to convert to speech: ") 
harsh = pyttsx3.init() # object creation
harsh.say(x) # text to speech
harsh.runAndWait() # run the speech engine
print("Thank you for using RoboSpeaker")



    
    
    
     
