
Options1 = input("Digite 1 para Encriptar ou 2 para Descriptar: ")

numbers = []
def lettersToNumbers():
  for element in letters:
    convertedNumber = ord(element) - 96
    numbers.append(convertedNumber)

def addToNumbers():
  addedNumbers = []
  for number in numbers:
      newNumber = number + 3
      addedNumbers.append(newNumber)
  return addedNumbers

def addedNumbersToBinary(array):
    binaryArray = []
    for addedNumber in array:
        newBinary = format(addedNumber, "b")
        binaryArray.append(newBinary)            
    return binaryArray

def reverseBinaryNumbers(binaryArrayCreated):
    reversedBinaryArray = []
    for i in binaryArrayCreated:
      stringList = list(i)
      stringList.reverse()
      stringList.append("100000001")
      reversedBinaryArray.append(stringList)
    return reversedBinaryArray

def arrayToString(array):
    encripted = []
    for i in array:
      string = "".join(str(x) for x in i)
      encripted.append(string)

    encripted = "".join(str(x) for x in encripted)
    print(encripted)
    return encripted

def binarytowords():
    listapalavras = ' '.join(phrase2[::-1] for phrase2 in phrase2.split("1100001" and "100000001"))            
    reversedList = listapalavras.split(" ")
    reversedList.pop()           
    return reversedList        

def binaryToDecimal(array):      
    decimal_rep = []
    for i in array:              
      decimal = int(i, 2)
      decimal_rep.append(decimal)            
    return decimal_rep

def decimalminus3(array):
    numSub = []
    for i in array:
      numSub.append(i-3)            
    return numSub

def numToLetter(array):
    newLetters = []
    for i in array:
      teste = i+96
      convertedNumber = chr(teste)
      newLetters.append(convertedNumber)                                        
    return newLetters
        
def joiningLetters(array):
    teste = ''.join(array)
    print(teste)

while (Options1 != "1" or Options1 != "2"):    
    if Options1 == "1":
        phrase = input("Insira o texto que deseja encriptar:\n")
        letters = list(phrase)
        lettersToNumbers()
        arrayToString(reverseBinaryNumbers(addedNumbersToBinary(addToNumbers())))
        break

    elif Options1 == "2":
        phrase2 = input("Insira o texto que deseja Descriptar:\n")
        joiningLetters(numToLetter(decimalminus3(binaryToDecimal(binarytowords()))))
        break
    else:
        Options1 = input("[ERRO] Valor digitado Invalido!\n Digite 1 para Encriptar ou 2 para Descriptar: ")