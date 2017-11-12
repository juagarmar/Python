# Python
def cifrado(Texto, Clave):
    Texto = str(Texto)
    Clave = int(Clave)
    cipher = list()
    for item in Texto:
        cipher.append(chr(ord(item)+Clave))  
    return ''.join(cipher)
print cifrado("hola pampliniiiii!", 4)
