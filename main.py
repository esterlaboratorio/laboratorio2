import operaciones


n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese un segundo numero: "))

print("♥ OPERACIONES MATEMATICAS♥")
print("""
1-Sumar
2-Restar
3-Multiplicacion
4-Division
5-Exponenciacion
6-Residuos
7-Raizes
""")
opcion=int(input("ingrese la operacion a realizar: "))
if opcion==1:
    print(operaciones.sumar(n1,n2))
if opcion==2:
    print(operaciones.restar(n1,n2))
if opcion==3:
    print(operaciones.mul(n1,n2))
if opcion==4:
    print(operaciones.div(n1,n2))
if opcion==5:
    print(operaciones.expo(n1,n2))
if opcion==6:
    print(operaciones.re(n1,n2))   
if opcion==7:
    print(operaciones.sqrt(n1,n2)) 

    


