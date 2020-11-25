#from math import *
import math

a= float(input("a="))
b= float(input("b="))
c= float(input("c="))
delta= b*b-4*a*c
if delta>=0:#wcięcie zaczyna instrukcję ze wcięciem
    p = math.sqrt(delta)
    x1=(-b-p)/(2*a)
    x2=(-b+p)/(2*a)
    print("x1={:6.2f}".format(x1)) #formatuje x, wypisz na 6-ściu miejscach,
    #2 miejsca po przecinku, float
    print("x2={:6.2f}".format(x2))
else:
    print("brak pierwiastków")

print(math.log(abs(x1)))

#int - napis
#float - liczba
#jeśli napiszemy
#pamiętać, żeby nie nazywać zmiennych jak funkcji np. cos
#jak importuje w sposób import math, to należy pamiętać o pisanu math.funkcja,
#nie tylko funkcje. Wtedy możemy zmienne nazywać jak funkcje z danej biblioteki

#python format w google - pyformat.info
