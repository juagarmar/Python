import re
texto1 = "hola buenos dias me llamo pepe!"
texto2 = "psss pa que me llamas si no quieres na!"
def contar_palabras_y_espacios(x):
    num_palabras = len(re.findall("[a-zA-Z_]+", x))
    num_espacios = x.count(' ')
    return num_palabras, num_espacios
print(contar_palabras_y_espacios(texto1))
print(contar_palabras_y_espacios(texto2))
"""num_palabras = len(re.findall(r'\w+', texto1))"""
