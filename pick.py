import re
import os

def cleanScreen():
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')

def presEnter(): # Pone el cartel de presione Enter para continuar y limpia la pantalla.
    print()
    input("Press Enter to continue...")
    cleanScreen()



# gets the path for the file

scriptDir = os.path.dirname(__file__) #<-- absolute dir the script is in
relPath = "kjb.txt"
absFilePath = os.path.join(scriptDir, relPath)

#open text file in read mode
textFile = open(absFilePath, "r")
 
#read whole file to a string
data = textFile.read()
 
#close file
textFile.close()

# asks for a letter, case sensitive

cleanScreen()
option = 100
while option != 0:
    print("  KJB Picker")
    print()
    print("  1 Run script")
    print("  0 Exit")
    print()
    option = int(input(" Choose an option: "))
    if option == 1:
        letter = input("\n Pick a letter: ")
# stores all words starting with the desired letter in a list
        word = re.findall(rf"\b{letter}\w+", data)
#prints the first letter
        print(f"\n The first word that starts with the letter {letter} is {word[0]} and repeats {len(word)} times.")
        presEnter()
    elif option == 0:
        print(" Goodbye")
        presEnter()
    else:
        print(" Incorrect option")
        presEnter()