import random

# modelo_objetivo = ['H', 'o', 'l', 'a', ' ', 'p', 'r', 'o', 'f', 'e']
modelo_objetivo = ['H', 'o', 'l', 'a']
modelo = [*map(lambda x: ord(x), modelo_objetivo)]
largo = len(modelo)
num = 15
pressure = 2
mutation_chance = 0.5

print(f"Modelo: {modelo_objetivo}")
print(f"Modelo (valor ASCII): {modelo}")


def individual(min_val: int, max_val: int) -> list[int]:
    """
        Crea un individuo
    """
    return [random.randint(min_val, max_val) for _ in range(largo)]


def crearPoblacion() -> list[list[int]]:
    """
        Crea una poblacion nueva de individuos
    """
    return [individual(ord('A'), ord('z')) for _ in range(num)]


def calcularFitness(individual):
    """
        Calcula el fitness de un individuo concreto.
    """
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1

    return fitness


def selection_and_reproduction(population):
    """
        Puntua todos los elementos de la poblacion (population) y se queda con los mejores
        guardandolos dentro de 'selected'.
        Despues mezcla el material genetico de los elegidos para crear nuevos individuos y
        llenar la poblacion (guardando tambien una copia de los individuos seleccionados sin
        modificar).

        Por ultimo muta a los individuos.

    """
    puntuados = [(calcularFitness(i), i) for i in population]
    puntuados = [i[1] for i in sorted(puntuados)]
    population = puntuados

    selected = puntuados[(
                                 len(puntuados) - pressure):]

    for i in range(len(population) - pressure):
        punto = random.randint(1, largo - 1)
        padre = random.sample(selected, 2)

        population[i][:punto] = padre[0][:punto]
        population[i][punto:] = padre[1][punto:]

    return population


def mutation(population):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    for i in range(len(population) - pressure):
        if random.random() <= mutation_chance:
            punto = random.randint(0, largo - 1)
            nuevo_valor = random.randint(1, 20)

            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1, 20)

            population[i][punto] = nuevo_valor

    return population


population = crearPoblacion()
print(f"Poblacion Inicial:")
print('\n'.join([*map(lambda entity: str([*map(lambda val: chr(val), entity)]), population)]))
target = 20000
for i in range(target):
    population = selection_and_reproduction(population)
    population = mutation(population)
    print(f"Progreso: {i}/{target}", end="\r")
print("\33[2K", end="")
print(f"Poblacion Final:")
print('\n'.join([*map(lambda entity: str([*map(lambda val: chr(val), entity)]), population)]))
