import math 
 
print("Szukamy liczb pierwszych.")
print("Podaj liczbę n: ")
n = int(input())
liczby = [True] * (n+1) 
for i in range(2, int(math.ceil(math.sqrt(n)))): 
    if liczby[i]: 
        for k in range(i*i, n+1, i): 
            liczby[k] = False
print("Liczby pierwsze z przedzialu <2,1000)" + str(n) + "> : ")
for i in range(2, n+1): 
    if liczby[i]:
        print(str(i), end=" | ")