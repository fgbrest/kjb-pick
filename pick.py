import re

#open text file in read mode
text_file = open("C:/Users/fgonz/OneDrive/Documentos/Dev/kjb-pick/kjb.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()

# asks for a letter, case sensitive

letra = input("Elegir una letra: ")

# stores all words starting with the desired letter in a list

palabra = re.findall(rf"\b{letra}\w+", data)

#prints the first letter

print(f"La primera palabra que empieza con la letra {letra} es {palabra[0]} y se repite {len(palabra)} veces.")