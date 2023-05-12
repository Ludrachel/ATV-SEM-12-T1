distancia_tartaruga = int(input())
distancia_lebre = 0
tempo_min = 0
while True:
    if distancia_tartaruga != 0:
        distancia_tartaruga += 1
        distancia_lebre += 10
        tempo_min += 1
    if distancia_tartaruga <= distancia_lebre:
        break
print(tempo_min)
