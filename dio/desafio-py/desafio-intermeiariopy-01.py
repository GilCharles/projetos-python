"""

- Desafio
Dada a letra N do alfabeto, nos diga qual a sua posição.


- Entrada
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).


- Saída
Um único inteiro, que representa a posição da letra no alfabeto.


Para codificações UTF-8 usar a subtração de -96
Para codificações ASCII usar a subtração de -64

"""

posicao = input()
print(ord(f"{posicao}") - 96)