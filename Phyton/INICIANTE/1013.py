## abs é uma função nativa do Python que retorna o valor absoluto de um número,
# ou seja, o valor numérico sem o sinal. Por exemplo, abs(-3) retorna 3, abs(3) retorna 3, e abs(0) retorna 0.
##No caso do cálculo (a + b + abs(a - b)) / 2, a função abs é utilizada para calcular a
# diferença entre a e b independentemente do sinal dessa diferença. Isso é importante porque, se a for menor que b,
# a diferença a - b será negativa, enquanto se a for maior que b, a diferença será positiva. Ao usar abs(a - b),
# o resultado será sempre o valor absoluto da diferença, que é o que interessa para encontrar o maior entre a e b.


a = float(input())
b = float(input())
c = float(input())

# Utiliza a fórmula para calcular o maior entre a e b
maior_ab = (a + b + abs(a - b)) / 2

# Compara o maior entre a+b e c para obter o maior valor entre os três
maior = (maior_ab + c + abs(maior_ab - c)) / 2

print(f"{maior} eh o maior")