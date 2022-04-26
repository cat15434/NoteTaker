from time import timezone
import speech_recognition as sr
from zoneinfo import ZoneInfo
import datetime as dt
inFile = False
fileName = ""

def getAudio():
 
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("SPeak")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        said = ""
       
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print (e)
    return said

if inFile == False:
    
    
    print("Running")
    said = getAudio()
    print(said)
    if said == "new file":
        print("File Name?")
        fileName = getAudio() + ".txt"
        print(fileName)
        with open(fileName,"a") as f:
            f.write(str(dt.date.today()))
            f.write("\n")
            time = dt.time(tzinfo=ZoneInfo("EST"))
            f.write('{:%H:%M}\n\n\n'.format(time))

            print("Running Text Appender")
            while True:
                 said = getAudio()
                 if said == "note completed":
                     f.close()
                     break
                 else:
                        wordCount = 0
                        words = said.split(' ')
                        for string in words:
                            wordCount +=1
                            print(wordCount)
                            f.write(string + " ")
                            if wordCount == 25:
                                f.write('\n')
                                wordCount = 0