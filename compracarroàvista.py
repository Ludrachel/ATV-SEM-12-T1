preco_carro = float(input())
poupanca = 10000
rendimento_poupanca = 0.007
taxa_carro = 0.004
meses = 0

while poupanca < preco_carro:
    poupanca += (poupanca * rendimento_poupanca)
    preco_carro += (preco_carro * taxa_carro)
    meses+= 1
print(meses)
