# Ćwiczenie 2:
# Dla podanej liczby groszy podaj najmniejszą liczbę monet,
# którą podaną sumę da się zrealizować.

a = int(input("Podaj liczbę groszy: "))

monety = [500,200,100,50,20,10,5,2,1]
liczba_monet = 0

for i in monety:
    liczba_monet += a // i
    a = a % i

print("najmniejsza liczba monet to:" , liczba_monet )
