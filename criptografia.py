# caixa de texto que recebera o texto
phrase = input("Insira o texto que deseja encriptar/decriptar:\n")
# separando a frase em letras, colocando em um array
letters = list(phrase)
# criando um array para os numeros
numbers = []

# definindo função para transformar letras em números, não podemos deixar que isso rode automaticamente pq na hora de decodificar ele faria isso e daria errado.


def lettersToNumbers():
    # essa função passa por todos os itens do array letters e transforma eles em números, se o número for negativo, ele arredonda, por exemplo espaço retorna -64, então transformamos ele em 64. O comando ord ja abrange também as letras maiusculas
    for element in letters:
        convertedNumber = ord(element) - 96
        if (convertedNumber < 0):
            convertedNumber = convertedNumber * -1

        numbers.append(convertedNumber)


# executando a função lettersToNumbers
lettersToNumbers()
# print(letters)
# print(numbers)

# definindo função que pega os numeros convertidos e adiciona +3 a cada um
def addToNumbers():
    addedNumbers = []
    for number in numbers:
        newNumber = number + 3
        addedNumbers.append(newNumber)
    # print(addedNumbers)
    return addedNumbers


def addedNumbersToBinary(array):
    binaryArray = []
    for addedNumber in array:
        newBinary = format(addedNumber, "b")
        binaryArray.append(newBinary)

    return binaryArray
    #binaryArray retorna o array com os numeros agora convertidos em binário

def reverseBinaryNumbers(binaryArrayCreated):
    reversedBinaryArray = []
    for i in binaryArrayCreated:
        stringList = list(i)
        stringList.reverse()
        reversedBinaryArray.append(stringList)
    print(reversedBinaryArray)



reverseBinaryNumbers(addedNumbersToBinary(addToNumbers()))


# def binaryInversion(listToArrays):


# Exemplo de execução do progama


# Insira o texto que deseja encriptar/decriptar:
# leo
#['l', 'e', 'o']
#[12, 5, 15]
#[15, 8, 18]
