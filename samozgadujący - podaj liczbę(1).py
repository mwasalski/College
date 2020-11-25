from random import randint

x = randint(1,6)
y = 0 #dodane jako 0, żeby program widział y ale nie brał go pod uwagę
#przed rozpoczęciem gry

a=1
b=100

while x!=y: #x!=y tzn x różne od y
    # y = int(input('podaj liczbę '))
    #y=randint(a,b)
    y=(a+b)//2
    if y<x:
        print('za mało')
        a=y
    elif y>x:
        print('za dużo')
        b = y

    
print('super, to było ', x)
#end while
