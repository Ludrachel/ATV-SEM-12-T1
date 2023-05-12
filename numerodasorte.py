data_nasc = int(input())

soma = 0

for i in range(8):
    caractere = data_nasc % 10
    soma += caractere
    data_nasc //= 10
    
print(soma)
