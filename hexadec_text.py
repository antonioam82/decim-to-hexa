from VALID import ns, OKI
import subprocess

def DecimalAHexadecimal(num):
    decimal = num
    hexadecimal = "" 
    while decimal != 0: 
        rem = CambiarDigitos(decimal % 16)
        hexadecimal = str(rem) + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal 

def CambiarDigitos(digitos):
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

while True:
    texto=input("Introduzca su texto aquí: ")
    lista_texto=list(texto)
    junt=[]
    for i in lista_texto:
        hexec=DecimalAHexadecimal(ord(i))
        junt.append(hexec)
        junt_text=("").join(junt)
    print(junt_text)
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
                
