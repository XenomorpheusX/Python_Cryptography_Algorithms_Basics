//Encrypt and Decrypt input value using Caesar Cipher. - Dora Avun

def encrypt(input, shift):
  result = "" #to return value
  for i in range(len(input)): #for all characters of input
    char = input[i] 
    if (char.isalpha()): #check if character is a letter
      if (char.isupper()): #check if the character is uppercase 
        result += chr((ord(char) + shift - 65) % 26 + 65)
        #Char to unicode(integer) to string. Also uppercase starts at 65.
      else:
         result += chr((ord(char) + shift - 97) % 26 + 97) #lowercase starts at 97
    else:
      result += char #bypass non-letter character
  return result

def decrypt(input, shift):
  result = ""
  for i in range(len(input)):
    char = input[i]
    if (char.isalpha()):#check if character is a letter
      if (char.isupper()): #check if the character is uppercase 
        result += chr((ord(char) - shift - 65) % 26 + 65) 
        #this time subtract the shift from unicode to decrypt
      else: 
        result += chr((ord(char) - shift - 97) % 26 + 97)
    else:
      result += char #bypass non-letter character
  return result

#to test the functions::
val = int(input("Choose an operation: 1-Encrypt, 2-Decrypt, 3-Quit\n"))
#interactive menu
if (val == 1):
  text = input("Enter text to Encrypt: ")
  shift = int(input("Enter the shift value: "))
  print ("Plain Text : " + text)
  print ("Shift pattern : " + str(shift))
  print ("Cipher: " + encrypt(text, shift))
elif (val == 2):
  text = input("Enter text to Decrypt: ")
  shift = int(input("Enter the shift value: "))
  print ("Cypher Text : " + text)
  print ("Shift pattern : " + str(shift))
  print ("Plain Text: " + decrypt(text, shift))
else:
  print ("forced quit")
