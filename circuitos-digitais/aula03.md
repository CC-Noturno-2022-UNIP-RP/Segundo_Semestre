# Binary-coded Decimal (BCD)

BCD é um sistema de numeração que codifica o sistema decimal pelo seu equivalente binário, dígito a dígito.

Exemplo:

35 -> 0011 0101

Observe que o BCD NÃO CORRESPONDE ao decimal convertido para binário. O BCD faz essa conversão cada unidade separadamente.

# American Standard Code for Information Interchange (ASCII)

ASCII é um sistema de representação de letras, algarismos, sinais de pontuação e de controle através de um código binário.

Desenvolvido a partir de 1960.

Possui 95 sinais gráficos, e 33 sinais de controle

Utiliza 7 bits

Exemplos de sinais gráficos:

32 -> SPACE
33 -> !
49 -> 1
50 -> 2
65 -> A
...

# Bit de Paridade

O bit de paridade serve para detectar o erro de 1bit em uma palavra binária.

Seja uma palavra binária de n bits da forma

O bit p de paridade par (ímpar) é acrescentado aos n bits de tal modo que o número de bits 1 seja par (ímpar)

<table border="1">
    <tr>
        <th>
        Exemplo
        </th>
        <th colspan="2">
        Paridade
        </th>
    </tr>
    <tr>
        <td>
        Palavra
        </td>
        <td>
        Par
        </td>
        <td>
        ímpar
        </td>
    </tr>
    <tr>
        <td>
        0110
        </td>
        <td>
        0110
        </td>
        <td>
        0110
        </td>
    </tr>
    <tr>
        <td>
        0101
        </td>
        <td>
        0101
        </td>
        <td>
        0101
        </td>
    </tr>
</table>

# Portas Lógicas

O estudo de portas lógicas começou em torno de 1960 com o CI, nos estudos de transistores (1942, EMAC). O transistor desligado representa 0 e ligado representa 1.

* Porta E (AND)

Tabela Verdade -> aberta quando as duas condições são verdadeiras.

* Porta OU (OR)

Tabela Verdade -> aberta quando qualquer uma das duas condições são verdadeiras.

* Porta NÃO (NOT) ou Porta inversora

Tabela Verdade -> retorna o oposto do valor inserido

* Porta OU-EXCLUSIVO (XOR)

Tabela Verdade -> retorna 0 se os dois dígitos forem iguais e 1 se forem diferentes