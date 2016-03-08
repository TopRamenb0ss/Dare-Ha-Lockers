import os
import time

print
print 'DARE HA LOCKERS'
print
print "typing anything other than what is prompted in this 'game' will result in termination"
print "you will be given four answers to chose from, do not try to type whatever you want"
print
presented = raw_input('start? (y/n): ')

while presented != "y" and "n":
    presented = raw_input("repeat your answer please: ")

    presented != "y" and "n"
if presented == 'n':
    print "then this should suit you well"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
firstLevel = raw_input("then let's see, type 'go' if you understand: ")
if firstLevel == 'go':
    firstTASK = raw_input("your lover informs you that they're a criminal, what do you do?  [enter]")
    print 'turn them in'
    print 'keep it a secret'
    print 'help them hide'
    print 'abandon them'
    firstAnswer = raw_input('your choice: ')
else:
    print "I see, then I'll excuse you from this program"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if firstAnswer == 'turn them in' or firstAnswer == 'keep it a secret' or firstAnswer == 'help them hide' or firstAnswer == 'abandon them':
    secondLevel = raw_input("very good, to proceed, type 'next': ")
    #questvar = 1
elif firstAnswer == "nate" or firstAnswer == "kari":
    print "to be honest, I'm proud that she still loves him for who he is"
    secondLevel = raw_input("you tried, to proceed, type 'next': ")
else:
    os.system("TASKKILL /F /IM pythonw.exe")
if secondLevel == 'next':
    secondTASK = raw_input("a friend of yours wants to have sex with you even though you're currently in a relationship, what do you do? [enter]")
    print 'deny consent'
    print 'give consent'
    print 'stall the conversation'
    print 'leave the conversation'
    secondAnswer = raw_input('your choice: ')
else:
    print "you must be busy with something else"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if secondAnswer == 'deny consent' or secondAnswer == 'give consent' or secondAnswer == 'stall the conversation' or secondAnswer == 'leave the conversation':
    thirdLevel = raw_input("you're doing well, type 'opfor' to continue: ")
    #questvar = 2
elif secondAnswer == "nate" or secondAnswer == "aki":
    print "being very honest to your partner is a good idea, which is why he unexpectedly gets the 'best boyfriend of 2087' award"
    thirdLevel = raw_input("secret hunter, huh, type 'opfor' to continue: ")
else:
     os.system("TASKKILL /F /IM pythonw.exe")   
if thirdLevel == "opfor":
    thirdTASK = raw_input("you used to be improsioned by a group of people and you later escaped from successfully, but would you risk being imprisoned again just to enact revenge? [enter]")
    print '"yes, revenge is perfect"'
    print '"no, I enjoy my freedom"'
    print '"only if the revenge is perfect enough"'
    print '"it depends"'
    thirdAnswer = raw_input('your choice: ')
else:
    print "if you will not answer the questions, then you are useless"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if thirdAnswer == '"yes, revenge is perfect"' or thirdAnswer == '"no, I enjoy my freedom"' or thirdAnswer == '"only if the revenge is perfect enough"' or thirdAnswer == '"it depends"':
    fourthLevel = raw_input("a picture is forming, type 'frame' to proceed: ")
    #questvar = 3
elif thirdAnswer == "simon":
    print "the foundation has been harsh on you, but yet you still seek exiting solace"
    fourthLevel = raw_input("a picture is being corrupted, type 'frame' to proceed: ")
else:
    os.system("TASKKILL /F /IM pythonw.exe")
if fourthLevel == 'frame':
    fourthTASK = raw_input("an intruder enters your house and threatens to shoot and kill you, if you could do anything successfully, what would it be? [enter]: ")
    print "disarm them"
    print "run away"
    print "reason with them"
    print "kill them"
    fourthAnswer = raw_input("your choice: ")
else:
    print "what a mistake your participation has been"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if fourthAnswer == "disarm them" or fourthAnswer == "run away" or fourthAnswer == "reason with them" or fourthAnswer == "kill them":
    fifthLevel = raw_input("you're halfway there, type 'half' if you wish to move on: ")
    #questvar = 4
elif fourthAnswer == "jacob" or fourthAnswer == "nate" or fourthAnswer == "kari":
    print "self defence at its finest, and its most critical"
    fifthLevel = raw_input("you're causing intrusion, type 'half' if you wish to move on: ")
else: 
    os.system("TASKKILL /F /IM pythonw.exe")
if fifthLevel == "half":
    fifthTASK = raw_input("your ex who violently broke up with you wants to call a truce and end hostilities for what they did, and you respond how? [enter]: ")
    print "accept it"
    print "refuse it"
    print "get mad"
    print "try to reform relationship"
    fifthAnswer = raw_input('your choice: ')
else:
    print "well, you tried"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if fifthAnswer ==  "accept it" or fifthAnswer == "refuse it" or fifthAnswer == "get mad" or fifthAnswer == "try to reform relationship":
    sixthLevel = raw_input("a puzzle is coming together, but the pieces don't match, type 'violence': ")
    #questvar = 5
elif fifthAnswer == "ren" or fifthAnswer == "nate":
    print "not only is he the best boyfriend ever, but he's the most humble, regaining the trust of hers"
    sixthLevel = raw_input("who are you, a guest, type 'violence': ")
else:
    os.system("TASKKILL /F /IM pythonw.exe")
if sixthLevel == "violence":
    sixthTASK = raw_input("a strange military vehicle is parked outside your penthouse, what is the next course of action? [enter]:")
    print "investigate it"
    print "ignore it"
    print "become worried about it"
    print "alert someone about it"
    sixthAnswer = raw_input('your choice: ')
else:
    print "what a rebel, you must be proud"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if sixthAnswer == "investigate it" or sixthAnswer == "ignore it" or sixthAnswer == "become worried about it" or sixthAnswer == "alert someone about it":
    seventhLevel = raw_input("or maybe I just don't like how they fit, type 'meltdown': ")
    questvar = 6
elif sixthAnswer == "mr nobody" or sixthAnswer == "scully":
    print "it happened all too fast, but with warning"
    seventhLevel = raw_input("why are you here, you are no guest of mine, type 'meltdown': ")
else:
    os.system("TASKKILL /F /IM pythonw.exe")
if seventhLevel == 'meltdown':
    seventhTASK = raw_input("you are busted out of jail by a friend who then takes you to an airport to fly to safety, how would you thank them? [enter]")
    print 'offer to complete a favor'
    print 'pay them'
    print 'display a lot of gratitude'
    print 'feel guilty because you have nothing to give'
    seventhAnswer = raw_input('your choice: ')
else:
    print "you must be a real hero, huh"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if seventhAnswer == 'offer to complete a favor' or seventhAnswer == 'pay them' or seventhAnswer == 'display a lot of gratitude' or seventhAnswer == 'feel guilty because you have nothing to give':
    eighthLevel = raw_input("nearing the end, gliding through the clouds, type 'dropzone': ")
    #questvar = 7
elif seventhAnswer == "jacob" or seventhAnswer == "aki":
    print "she was always in his debt, until he was murdered in self defense"
    eighthLevel = raw_input("maybe you forgot a chute because you're so nosy, type 'dropzone': ")
else:
    os.system("TASKKILL /F /IM pythonw.exe")
if eighthLevel == "dropzone":
    eighthTASK = raw_input("as you help out a close friend in their home, they notice that your private conversation has been tapped and recorded, what do you do? [enter]: ")
    print 'exit the home'
    print 'report to police'
    print 'destroy the device'
    print 'keep it a secret'
    eighthAnswer = raw_input('your choice: ')
else:
    print "rather you leave than cause more harm"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if eighthAnswer == 'exit the home' or eighthAnswer == 'report to police' or eighthAnswer == 'destroy the device' or eighthAnswer == 'keep it a secret':    
    ninthLevel = raw_input("almost done, rather a masterpiece is being forged, type 'nonono': ")    
    #questvar = 8
elif eighthAnswer == "kari" or eighthAnswer == "nate":
    print "it takes such an event to kill all tension, it was a very bold move myself"
    ninthLevel = raw_input("very close, you're the masterpiece itself, type 'nonono': ")    
else:
    os.system("TASKKILL /F /IM pythonw.exe")
if ninthLevel == "nonono":
    ninthTASK = raw_input("while in a secret group with only four people, you find out that one of them is a traitor [enter]: ")
    print "make them leave"
    print "kill them"
    print "kill them"
    print "kill them"
    ninthAnswer = raw_input('your choice: ')
else:
    print "futile, futile, futile"
    time.sleep(4)
    os.system("TASKKILL /F /IM pythonw.exe")
if ninthAnswer == "make them leave" or ninthAnswer == "kill them":
    tenthLevel = raw_input("you are about to finish, type 'noexit': ")
    #questvar = 9
elif ninthAnswer == "jacob" or ninthAnswer == "nate" or ninthAnswer == "ren" or ninthAnswer == "aki":
    print "there was no other option"
    tenthLevel = raw_input("you are about to finish, type 'noexit': ")

while tenthLevel != "noexit":
    tenthLevel = raw_input("there is no exit, admit it: ")

    tenthLevel != "noexit"
    
if tenthLevel == 'noexit':
    tenthTASK = raw_input("your two friends are bleeding out and THEY are coming for all three of you, they will slaughter you, you have the choice to spare them the pain with one bullet each [enter]: ")
    print "spare them"
    print "kill them"
    tenthAnswer = raw_input('if you could change the past: ')
if tenthAnswer == "spare them" or tenthAnswer == "kill them" or tenthAnswer == "marius" or tenthAnswer == "dominic" or tenthAnswer == "kari":
    print
    sans = raw_input("you will now be judged [enter]: ")
    print
    questvar = 10
elif tenthAnswer == "frost":
    raw_input('despite if you know secrets and the like, you will now be judged: ')

if firstAnswer == 'turn them in' or firstAnswer == 'keep it a secret' or firstAnswer == 'help them hide' or firstAnswer == 'abandon them':
    print "if you found out your lover was a criminal, you would " + firstAnswer
elif firstAnswer == "nate" or firstAnswer == "kari":
    print "collapsing, part 1"
if secondAnswer == 'deny consent' or secondAnswer == 'give consent' or secondAnswer == 'stall the conversation' or secondAnswer == 'leave the conversation':
    print "if a good friend of yours wanted you to cheat on your current lover, you would " + secondAnswer
elif secondAnswer == "nate" or secondAnswer == "aki":
    print "late night conversation, iteration c"
if thirdAnswer == '"yes, revenge is perfect"' or thirdAnswer == '"no, I enjoy my freedom"' or thirdAnswer == '"only if the revenge is perfect enough"' or thirdAnswer == '"it depends"':
    print "even if you could be re-imprisoned by the same people, " + thirdAnswer + " seemed like a good way to think about revenge"
elif thirdAnswer == "simon":
    print "incident 3000-148-3"
if fourthAnswer == "disarm them" or fourthAnswer == "run away" or fourthAnswer == "reason with them" or fourthAnswer == "kill them":
    print "if you were a victim of home invasion at gunpoint, you would just " + fourthAnswer + " anyways"
elif fourthAnswer == "jacob" or fourthAnswer == "nate" or fourthAnswer == "kari":
    print "apocalypse"
if fifthAnswer ==  "accept it" or fifthAnswer == "refuse it" or fifthAnswer == "get mad" or fifthAnswer == "try to reform relationship":
    print "if your ex were to try to make friends again, your response to the offer would be to " + fifthAnswer
elif fifthAnswer == "ren" or fifthAnswer == "nate":
    print "apology conversation, iteration b"    
if sixthAnswer == "investigate it" or sixthAnswer == "ignore it" or sixthAnswer == "become worried about it" or sixthAnswer == "alert someone about it":
    print "on the event a military vehicle parks outside your home, you would " + sixthAnswer
elif sixthAnswer == "mr nobody" or sixthAnswer == "scully":
    print "ho ho ho"
if seventhAnswer == 'offer to complete a favor' or seventhAnswer == 'pay them' or seventhAnswer == 'display a lot of gratitude' or seventhAnswer == 'feel guilty because you have nothing to give':
    print "lucky enough to have such a friend, they broke you out of jail and as a thanks you would " + seventhAnswer
elif seventhAnswer == "jacob" or seventhAnswer == "aki":
    print "release"
if eighthAnswer == 'exit the home' or eighthAnswer == 'report to police' or eighthAnswer == 'destroy the device' or eighthAnswer == 'keep it a secret':    
    print "while helping out a friend and listening to their conversation, and if they found out that you two were being recorded, you would " + eighthAnswer
elif eighthAnswer == "kari" or eighthAnswer == "nate":
    print "collapsing, part 2"
if ninthAnswer == "make them leave" or ninthAnswer == "kill them":
    print "there is a traitor in your group, and you thought that you would " + ninthAnswer
elif ninthAnswer == "jacob" or ninthAnswer == "nate" or ninthAnswer == "ren" or ninthAnswer == "aki":
    print "caught"
if tenthAnswer == "spare them" or tenthAnswer == "kill them":  
    print "a choice to let your friends be slaughtered while they bleed out or to shoot them with one fatal round, you would " + tenthAnswer
elif tenthAnswer == "marius" or tenthAnswer == "dominic" or tenthAnswer == "kari":
    print "i'm sorry"
print
print "thank you for participating the 'Hacker's Ordeal' and enjoy having your personality logged into my database"
print "made special for ignorant people like you to answer- A/B"
print