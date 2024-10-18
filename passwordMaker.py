import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
uppercaseLetter3=chr(random.randint(65,90)) 
uppercaseLetter4=chr(random.randint(65,90)) 
uppercaseLetter5=chr(random.randint(65,90)) 
uppercaseLetter6=chr(random.randint(65,90)) 
uppercaseLetter7=chr(random.randint(65,90)) 
uppercaseLetter8=chr(random.randint(65,90)) 
uppercaseLetter9=chr(random.randint(65,90)) 
uppercaseLetter10=chr(random.randint(65,90)) 


#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 + uppercaseLetter8 + uppercaseLetter9 + uppercaseLetter10 
password = shuffle(password)

#Ouput
print(password)