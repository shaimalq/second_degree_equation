import math
A=float(input("entrer la valeur de A:"))
B=float(input("entrer la valeur de B:"))
C=float(input("entrer la valeur de C:"))
delta=(B**2)-4*A*C
if delta<0:
    print("Pas de solution reelles")
elif delta==0:
    x=(-B)/2*A
    print("la solution est:",x)
else:
    x1=(-B-math.sqrt(delta))/2*A
    x2=(-B+math.sqrt(delta))/2*A
    print("les solutions sont:",x1,x2)
