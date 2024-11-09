dohod = int(input())    #доход
ns = int(input())       #налоговая ставка(%)

tax_amount = dohod * (ns / 100)
result = dohod - tax_amount
print(int(result))