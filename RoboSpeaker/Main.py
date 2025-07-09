import pyttsx3
import os

if __name__ == '__main__':
    # start main program from here
    # meaning of this line is that if this file is run as main program then only run the following code

    print("🎙️ welcome to RoboSpeaker")
    folder = "saved_audio"
    os.makedirs(folder, exist_ok=True)


    try:
        while True:
            x = input("Enter the text you want to convert to speech: ")

            if x.lower() == 'exit':
                print("Exiting RoboSpeaker. Goodbye! 👋")
                break
# ✍️ Save text to transcript file
            with open("transcript.txt", "a", encoding="utf-8") as log:
             log.write(x + "\n")
            
            harsh = pyttsx3.init()  # object creation
            harsh.setProperty('rate', 100)  # setting up the speed of speech
            harsh.setProperty('volume', 1)  # setting up the volume of speech

            save = input("Do you want to save the speech to a file? (yes/no): ").lower()
            
            if save in ['yes', 'y']:
                
                filename = input("Enter a custom file name (without extension): ").strip()
                if not filename:
                    filename = "output"
                if not filename.lower().endswith(".mp3"):
                    filename += ".mp3"
                full_path = os.path.join(folder, filename)

                # Check if file already exists
                if os.path.exists(full_path):
                    overwrite = input("⚠️ File exists. Overwrite? (yes/no): ").lower()
                    if overwrite != 'yes':
                        print("❌ File not saved.")
                        continue
                harsh.save_to_file(x, filename)
                harsh.runAndWait()  # run the speech engine to save the file
                print(f"Speech saved to {filename}")

            else:
                harsh.say(x)
                harsh.runAndWait()  # run the speech engine
            print("Thank you for using RoboSpeaker")
    except KeyboardInterrupt:
        print("\n👋 Exiting RoboSpeaker. Goodbye!")
