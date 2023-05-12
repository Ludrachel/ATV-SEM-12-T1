qtd_populacao = int(input())

ano = 1600

popu_total = qtd_populacao * 0.1

while True:
    nasc = int(qtd_populacao * 0.01)
    mortes = int(qtd_populacao * 0.06)
    qtd_populacao += (nasc - mortes)
    print(f'{ano},{int(nasc)},{int(mortes)},{int(qtd_populacao)}')
    ano += 1

    if qtd_populacao < popu_total:
        break
    
    

