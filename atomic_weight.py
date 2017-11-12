import re

# Grupos de varias letras, seguidas (o no) de números
pat = re.compile("([a-zA-Z]+)(\d*)")  
masas = {'H': 1.007825, 'C': 12.01, 'O': 15.9994, 'N': 14.0067, 'S': 31.972071, 
'P': 30.973762}

def calcula_masa_atomica(molecula):
    grupos = [(atom, int(n) if n else 1) 
                 for (atom, n) in pat.findall(molecula)]

    masa = sum(n*masas.get(atom,0.0) for (atom,n) in grupos)
    return masa
print calcula_masa_atomica('C2-H4-O')

https://es.stackoverflow.com/questions/31522/duda-python-bucle-split-y-m%C3%A1s
