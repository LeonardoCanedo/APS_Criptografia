# caixa de texto que recebera o texto
Options1 = input("Digite 1 para Encriptar ou 2 para Descriptar: ")
#enquanto a pessoa nao inserir 1 ou 2 mostra mensagem de erro e volta para o inicio do código
while (Options1 != "1" or Options1 != "2"):    
    if Options1 == "1":
        phrase = input("Insira o texto que deseja encriptar:\n")
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
            return reversedBinaryArray

        def arrayToString(array):
            encripted = []
            for i in array:
                string = "".join(str(x) for x in i)
                encripted.append(string)

            encripted = "".join(str(x) for x in encripted)
            print(encripted)
            return encripted


        arrayToString(reverseBinaryNumbers(addedNumbersToBinary(addToNumbers())))

    elif Options1 == "2":
        phrase2 = input("Insira o texto que deseja Descriptar:\n")
        #essa funçao faz com que toda a frase encripitada seja separada no número "1100001" e cria uma lista separada com os resultados restantes.
        def binarytowords():
            listapalavras = phrase2.split("1100001")            
            print(listapalavras)
            return listapalavras
            
        binarytowords()
          
    else:
        Options1 = input("[ERRO] Valor digitado Invalido!\n Digite 1 para Encriptar ou 2 para Descriptar: ")

