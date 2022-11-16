# APS_Criptografia
Trabalho APS UNIP 2º Semestre

O GitHub vai nos ajudar a nos comunicar sobre o que esta técnicamente acontecendo aqui no código/estrutura do projeto, ai ninguém fica perdido :)
Vamos usar esse arquivo read.me para fazer uma descrição melhor do projeto, com as partes, explicações, etc.

Quando vocês fizerem alguma modificação no código e forem atualizar, vocês fazem um commit aqui nesse repositório para atualizar o arquivo para todo mundo, e nesse commit você descreve o que você fez ou bugs que resolveu/ainda tem que resolver.

Nosso algoritimo de criptografia trabalha com conversão de tipos (String, Int) e conversão de bases (Decimal, binária)

A principio o algoritimo tem que funcionar assim:

while com 3 opcoes - 1 => codificar, 2 => decodificar, 3 => mensagem de erro volta pro while.

Codificar
  Letra => Número => Número + 3 => Binário => Inversão => print
  Na codificação colocamos um certo separador para identificarmos o final de cada frase.
 
Decodificar
  Input codificado => split "1100001" (espaço) => Separar com split o separador => lista criada pelos splits => numero => número -3 => letra/palavra



