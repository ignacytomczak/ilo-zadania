# Wprowadź liczbę całkowitą n.
# Policz sumę liczb od 1 do n włącznie

n = int(input("Podaj liczbę całkowitą n: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print("Suma liczb od 1 do n:", suma)
