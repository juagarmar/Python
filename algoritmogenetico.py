# Cargamos los paquetes necesarios para generas números aleatorios y para trabajar con filas de datos
import random
import string

# Definimos la variable objetivo, genes y max_generation
objetivo = "Espero aprobar esta asignatura"

#Como la cadena elejida en este caso es más larga que la del ejemplo aumentamos el número de GENES y de MAX_GENERACION.
GENES = 20
MAX_GENERACION = 6000

# El fitness es una medida de los individuos mejor adaptados, esta medida será mejor cuanto menor sea el valor de fitness
# Creamos la clase "Individuo con la caracteristica fitness, la cual indica como de adaptado se encuentra indirectamente proporcional al valor fitness.
class Individuo(object):
    def __init__(self, adn, fitness):
        self.adn = adn
        self.fitness = fitness

# Esta función compara el individuo origen con el objetivo en orden de calcular la diferencia entre estas cadenas.
def calcular_fitness(origen, valor_objetivo):
    fitness = 0
    for i in range(0, len(origen)):
        fitness += (ord(valor_objetivo[i]) - ord(origen[i])) ** 2
    return fitness

# A Continuación emplearemos las variables padre1/2 para determinar los datos de origen obtenidos aleatoriamente mediante la función "randint" de manera que al mezcla al azar obtengamos el valor hijo.
# Esta función será empleada posteriormente en la función "simulacion" para determinar la variable hijo (hijo = mutacion(padre1, padre2))
def mutacion(padre1, padre2):
    adn_hijo = padre1.adn[:]

    start = random.randint(0, len(padre2.adn) - 1)
    stop = random.randint(0, len(padre2.adn) - 1)
    if start > stop:
        stop, start = start, stop

    adn_hijo[start:stop] = padre2.adn[start:stop]

    posicion = random.randint(0, len(adn_hijo) - 1)
    adn_hijo[posicion] = chr(ord(adn_hijo[posicion]) + random.randint(-1, 1))
    fitness_hijo = calcular_fitness(adn_hijo, objetivo)
    return Individuo(adn_hijo, fitness_hijo)

# Para obtener la población definimos la siguiente función para obtener 20 individuos al azar. Estos nos dará como resultados que posteriormente usaremos en la función simulación.

def padre_al_azar(poblacion):
    return poblacion[int(random.random() * random.random() * (GENES - 1))]

# Muestra los pasos de la simulacion, el fitness y el ADN de cada gen.

def escribe_generacion(generacion, poblacion):
    print 'Pasos de simulación: %d' % generacion
    print
    print '  Fitness         ADN'
    print '------------------------'
    for candidato in poblacion:
        print "%6i %15s" % (candidato.fitness, ''.join(candidato.adn))
    print

# Siendo la variable "poblacion" una lista vacia. 
# Creamos con la siguiente formula los 20 primeros genes con la misma longitud que nuestra secuencia objetivo.
# Definimos fitness, adn y candidate para estos 20 valores. el objetivo es crear la variables candidate a la cual aplicaremos la función.

def inicializa_poblacion():
    poblacion = []
    for i in range(0, GENES):
        adn = [random.choice(string.printable[:-5]) for _ in range(0, len(objetivo))]
        fitness = calcular_fitness(adn, objetivo)
        candidate = Individuo(adn, fitness)
        poblacion.append(candidate)
    return poblacion

# Finalmente llegamos a la función "simulacion". 
# Partiendo de una lista poblacion como argumentos en la función padre_al_azar (padre1 / padre2)
# Estableciendo como límite el número maximo de generaciones o "MAX_GENERATION"
# Comparamos los valores fitness entre las poblaciones y sustituimos la variable hijo por aquella con menor valor "fitness".
def simulacion():
# Determinamos la población mediante la formula anterior.
    poblacion = inicializa_poblacion()
# Definimos el inicio de nuestras iteraciones.
    generacion = 0
# Establecemos el límite.
    while True and generacion < MAX_GENERACION:
        generacion += 1
        poblacion.sort(key=lambda candidate: candidate.fitness)

        if poblacion[0].fitness == 0:
            break
# Definimos padre1/2 mediante la formula "padre_al_azar".
        padre1 = padre_al_azar(poblacion)
        padre2 = padre_al_azar(poblacion)
# Definimos las variable hijo mediante la formula "mutacion".
        hijo = mutacion(padre1, padre2)
        if hijo.fitness < poblacion[-1].fitness:
            poblacion[-1] = hijo
# Establecemos el límite.
    if generacion == MAX_GENERACION:
        print u'Se ha alcanzado el máximo de generaciones'
    escribe_generacion(generacion, poblacion)


simulacion()
