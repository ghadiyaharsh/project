import pyttsx3

if __name__ == '__main__':
    # start main program from here
    # meaning of this line is that if this file is run as main program then only run the following code

    print("🎙️ welcome to RoboSpeaker")
    
    counter = 1  # Initialize a counter for file naming

    try:
        while True:
            x = input("Enter the text you want to convert to speech: ")

            if x.lower() == 'exit':
                print("Exiting RoboSpeaker. Goodbye! 👋")
                break

            harsh = pyttsx3.init()  # object creation
            harsh.setProperty('rate', 100)  # setting up the speed of speech
            harsh.setProperty('volume', 1)  # setting up the volume of speech

            save = input("Do you want to save the speech to a file? (yes/no): ").lower()
            if save in ['yes', 'y']:
                filename = f"output_{counter}.mp3"
                harsh.save_to_file(x, filename)
                harsh.runAndWait()  # run the speech engine to save the file
                print(f"Speech saved to {filename}")
            else:
                harsh.say(x)
                harsh.runAndWait()  # run the speech engine
            print("Thank you for using RoboSpeaker")
            counter += 1
    except KeyboardInterrupt:
        print("\n👋 Exiting RoboSpeaker. Goodbye!")
