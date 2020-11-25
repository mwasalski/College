from random import randint

x = randint(1,6)
y = 0 #dodane jako 0, żeby program widział y ale nie brał go pod uwagę
#przed rozpoczęciem gry

while x!=y: #x!=y tzn x różne od y
    y = int(input('podaj liczbę '))
    if y<x:
        print('za mało')
    elif y>x:
        print('za dużo')
    else:
        print('super')

    
print('koniec')
#end while
