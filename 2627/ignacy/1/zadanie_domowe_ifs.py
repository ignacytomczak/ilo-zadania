# Napisz program, który dla wprowadzonych liczb x, y porównuje x * y oraz x + y
# Wypisz w odpowiednich przypadkach "są równe", "iloczyn jest większy", "suma jest większa"

x = int(input("Podaj liczbę całkowitą x: "))
y = int(input("Podaj liczbę całkowitą y: "))

iloczyn = x * y
suma = x + y

if iloczyn > suma :
    print("iloczyn jest większy")

elif suma > iloczyn :
    print("suma jest większa")

else :
    print("są równe")
