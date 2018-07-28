from VALID import OKI, ns
import subprocess
#CONVERTIR DECIMAL EN HEXADECIMAL

while True:
    def DecimalAHexadecimal():
        decimal = OKI(input("Introduzca número: "))
        hexadecimal = ""
        while decimal != 0: 
            rem = CambiarDigitos(decimal % 16)
            hexadecimal = str(rem) + hexadecimal
            decimal = int(decimal / 16)
        print("Resultado: " + hexadecimal) 

    def CambiarDigitos(digitos):
        decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
        hexadecimal = ["A", "B", "C", "D", "E", "F"]
        for c in range(7):
            if digitos == decimales[c - 1]:
                digitos = hexadecimal[c - 1]
        return digitos

    DecimalAHexadecimal()
    conti=ns(input("¿Desea continuar?: "))

    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
