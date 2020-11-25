#12 -> 1+2+3+4+6=16

def sp(n): #sp= suma podzielników
    'funckja zwraca sumę podzielników właściwych' # łańcuch dokumentujący
    suma = 0
    for p in range(1,n):
     if n%p==0: #reszta z dzielenia = 0
      suma += p #suma zwiększ o p
      
    return suma
# koniec definicji funkcji

for x in range(1,20):
    if x==sp(x):
        print(x, sp(x))
     else
        print('nic nie ma')
