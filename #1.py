a= float(input("a="))
b= float(input("b="))
c= float(input("c="))
d= b*b-4*a*c
if d>=0:#wcięcie zaczyna instrukcję ze wcięciem
    p = sqrt(d)
    x1=(-b-p)/(2*a)
    x2=(-b+p)/(2*a)
    print(x1,x2)
else:
    print("brak pierwiastków")

#int - napis
#float - liczba
