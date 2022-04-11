//Decrypt a plaintext using Feistel Cipher Method - Dora Avun.

import random
def keyGenerator(x): #to generate keys for rounds
  key = ""        
  for i in range(int(x)):         
    temp = str(random.randint(0,1))
    key = key + temp   
  return(key)
 
def BinaryToDecimal(binary): #to convert decimal to binary
  result = int(binary, 2)       
  return result

def xor(a,b): # to xor the strings 
  temp = ""     
  for i in range(n):        
      if (a[i] == b[i]): #compare each char of strings
          temp += "0"             
      else:
          temp += "1"             
  return temp
 
text = "Hello World"
PT_Ascii = [ord(x) for x in text] #convert to ASCII by using ord(x) for each letter in string
PT_Bin = [format(y,'08b') for y in PT_Ascii] #format the ASCII to 8bit
PT_Bin = "".join(PT_Bin)
#divide the 8 bit format into two halves L1 and R1
n = int(len(PT_Bin)//2) 
L1 = PT_Bin[0:n]
R1 = PT_Bin[n::]
m = len(R1)

#generate keys
K1= keyGenerator(m)
K2= keyGenerator(m)  
# Round 1
f1 = xor(R1,K1)
R2 = xor(f1,L1)
L2 = R1  
# Round 2
f2 = xor(R2,K2)
R3 = xor(f2,L2)
L3 = R2

cipherText = L3 + R3 #combine left and right results
strCipher =' '
 
for i in range(0, len(cipherText), 7):
  temp = cipherText[i:i + 7] #slice and store PT_Bin
  decimal = BinaryToDecimal(temp) #convert to decimal
  strCipher = strCipher + chr(decimal) #return the corresponding string
  
print("Plain Text is:", text)     
print("Cipher Text:", strCipher)
 
