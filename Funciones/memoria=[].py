memoria=[]

def suma(n1 , n2):
    total=0
    for i in range(n):
        numero=int(input("Ingrese numero." , i+1))
        total+=numero

    return total

def resta(n1 , n2):
    return

while True:
    print("---- Calculadora ----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    op=input("Digite la opcion deseada del menu: ")

    match op:
        case '1':
            res=suma(int(input("Ingrese cantidad de numeros a sumar: ")))
            memoria.append(res)

        case '2':
            print()
        
        case '5':
            print("Usted salio del sistema")
            break
        
        case _:
            print("Opcion no valida")