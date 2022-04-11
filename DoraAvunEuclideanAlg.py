//Calculate the GCD between 2 values using Euclidean Algorithm. - Dora Avun

def gcdCalculate(a, b):
  remainder=a%b #set the remainder
  while remainder: #until the remainder is 0, loop
      a = b
      b = remainder
      remainder = a % b
  return abs(b)  #return positive value regardless the output
  
a = int(input("Please enter the first number to calculate: "))
b = int(input("Please enter the second number to calculate: ")) 
print ("GCD of values ", a, ", ",b, "is: ", gcdCalculate(a, b))