popu_A = int(input())
popu_B = int(input())
anos = 0

if popu_B > popu_A:
    while popu_B > popu_A:
        popu_B *= 1.02
        popu_A *= 1.03
        anos += 1
else:
    while popu_A > popu_B:
         popu_A *= 1.03
         popu_B *= 1.02
         anos += 1
         
print(anos)
        
