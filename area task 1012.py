A,B,C=[float(X) for X in input().split()]
TRIANGULO=(A*C)/2
print("TRIANGULO:",'{:.3f}'.format(TRIANGULO))
pi=3.14159
ac=pi*(C**2)
print("CIRCULO:",'{:.3f}'.format(ac))
at=((A+B)*C)/2 
print("TRAPEZIO:",'{:.3f}'.format(at))
aq=B**2
print("QUADRADO:",'{:.3f}'.format(aq))
ar=A*B
print("RETANGULO:",'{:.3f}'.format(ar))