n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2+3+4+1)
print(f"Media final: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado. ")
elif media < 5.0:
    print("Aluno reprovado. ")
elif 5 <= media <= 6.9:
    print("Aluno em exame. ")