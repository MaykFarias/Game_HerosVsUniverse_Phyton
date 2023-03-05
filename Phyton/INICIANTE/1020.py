dia = int(input())

#Pega o Resultado da Divisão
ano = dia // 365
#Pega o Resto dda Divisão
dia = dia % 365

#Pega o Resultado da Divisão
mes = dia // 30
#Pega o Resto dda Divisão
dia = dia % 30

print(f"{ano} ano (s)")
print(f"{mes} mes (es)")
print(f"{dia} dia (s)")
