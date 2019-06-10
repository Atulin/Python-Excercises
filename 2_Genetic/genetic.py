import random


MAX_BITS = 5


# Make an array of bits from an int
def int_to_bitarray(n: int) -> list:
    arr = [1 if digit == '1' else 0 for digit in bin(n)[2:]]
    padding = [0] * (MAX_BITS - len(arr))
    return padding + arr


# Make an int from an array of bits
def bitarray_to_int(bits: list) -> int:
    out = 0
    for bit in bits:
        out = (out << 1) | bit
    return out


# Class describing the specimen and its properties
class Specimen(object):
    value: int = 0
    bit_value: list = []
    fitness: float = 0.0

    def __init__(self, value: int):
        self.value = value
        self.bit_value = int_to_bitarray(value)
        super().__init__()

    def __str__(self) -> str:
        return 'val:' + str(self.value) + '|bit:' + str(self.bit_value) + '|fit:' + str(self.fitness)

    def calculate_fitness(self, a: int, b: int, c: int, d: int):
        v = self.value
        self.fitness = (a * pow(v, 3)) + (b * pow(v, 2)) + (c * v) + d

    def mutate(self):
        r = round(random.random() * (len(self.bit_value) - 1))
        self.bit_value[r] = 0 if self.bit_value[r] == 1 else 1
        self.value = bitarray_to_int(self.bit_value)


# Cross specimen
def cross(specimen_a: 'Specimen', specimen_b: 'Specimen', cross_position: int) -> tuple:
    arr_a = specimen_a.bit_value
    arr_b = specimen_b.bit_value

    arr_a_new = [None] * len(arr_a)
    arr_b_new = [None] * len(arr_b)

    for m in range(0, cross_position):
        arr_a_new[m] = arr_a[m]
        arr_b_new[m] = arr_b[m]

    for n in range(cross_position, len(arr_a)):
        arr_a_new[n] = arr_b[n]
        arr_b_new[n] = arr_a[n]

    specimen_a_new = Specimen(bitarray_to_int(arr_a_new))
    specimen_b_new = Specimen(bitarray_to_int(arr_b_new))

    return specimen_a_new, specimen_b_new


# Roulette selection
def roulette(specimen: list):
    roul = [0] * (len(specimen) + 1)
    surviving_indexes = [0] * len(specimen)
    last_index = len(specimen) - 1

    min_val: Specimen = min(specimen, key=lambda x: x.fitness)

    # Make sure all values are more than 0 but stay proportional
    if min_val.fitness < 0:
        for s in specimen:
            s.fitness += abs(min_val.fitness * 2)

    # Create a Fibonacci-like sequence of weights
    for r in range(1, len(roul)):
        roul[r] = roul[r - 1] + specimen[r - 1].fitness

    # Use the calculated weights to select surviving indexes
    for si in range(0, len(surviving_indexes)):
        rnd = random.random() * roul[last_index]

        for sj in range(0, len(roul) - 1):
            if roul[sj] <= rnd < roul[sj + 1]:
                surviving_indexes[si] = sj

    return surviving_indexes


# Generate random starting population
def generate_random_pop(amount: int, a: int, b: int, c: int, d: int) -> list:
    pop = [Specimen(0)] * amount
    _max = [1] * MAX_BITS

    for p in range(0, amount):
        pop[p] = Specimen(random.randint(0, bitarray_to_int(_max)))
        pop[p].calculate_fitness(a, b, c, d)

    return pop


# Apply roulette results to the population
def roulette_population(specimen: list, roul: list) -> list:
    new_pop = [Specimen(0)] * len(specimen)

    for i in range(0, len(specimen)):
        new_pop[i] = specimen[roul[i]]

    return new_pop


# Try crossing specimen in the whole population to create offspring
def cross_population(specimen: list, crossing_chance: int, a: int, b: int, c: int, d: int) -> list:
    result = [Specimen(0)] * len(specimen)

    for i in range(0, len(specimen), 2):
        chance = random.randint(0, 100)
        position = random.randint(0, MAX_BITS)

        # Check for lonely specimen
        if i + 1 < len(specimen):

            # Check crossing chance and cross
            if chance < crossing_chance:
                s = cross(specimen[i], specimen[i + 1], position)
                result[i] = s[0]
                result[i + 1] = s[1]
            else:
                result[i] = specimen[0]
                result[i + 1] = specimen[1]
        else:
            result[i] = specimen[1]

    for r in result:
        r.calculate_fitness(a, b, c, d)

    return result


# Try mutating specimen in the population
def mutate_population(specimen: list, mutation_chance: int, a: int, b: int, c: int, d: int) -> list:
    result = [Specimen(0)] * len(specimen)

    for i in range(0, len(specimen)):
        chance = random.randint(0, 100)

        if chance <= mutation_chance:
            specimen[i].mutate()
            result[i] = specimen[i]
        else:
            result[i] = specimen[i]

    for r in result:
        r.calculate_fitness(a, b, c, d)

    return result


# Run the genetic algorithm
def genetic(amount: int, max_iterations: int, stop_condition: int, cross_chance: int, mutation_chance: int,
            a: int, b: int, c: int, d: int):
    specimen = generate_random_pop(amount, a, b, c, d)
    best_fitnesses = []

    for cnt in range(0, max_iterations):
        best_specimen = max(specimen, key=lambda x: x.fitness)

        same_fitness = 0

        print()
        print("Generation %s:" % cnt)
        print("Best specimen: %s" % best_specimen)

        # Check for how many iterations the result was the same
        for sc in reversed(range(0, stop_condition + 1)):
            if len(best_fitnesses) > stop_condition:
                if best_fitnesses[len(best_fitnesses) - 1 - sc] == best_specimen.fitness:
                    same_fitness += 1

        # If it was the same too long, break out
        if same_fitness > stop_condition:
            break

        # Add current best fitness to the list of best fitnesses
        best_fitnesses.append(best_specimen.fitness)

        for s in range(0, len(specimen)):
            print("[S-%s] %s" % (s + 1, specimen[s]))

        # Create roulette
        rou = roulette(specimen)
        # Apply it
        specimen = roulette_population(specimen, rou)
        # Cross the population
        specimen = cross_population(specimen, cross_chance, a, b, c, d)
        # Mutate the population
        specimen = mutate_population(specimen, mutation_chance, a, b, c, d)


# Run the program
def run():
    amount = int(input("Desired amount of specimen: "))
    loops = int(input("Maximum number of iterations: "))
    cond = int(input("After how many iterations of no fitness change should the algorithm stop: "))
    cross = int(input("Chance for two specimen to have offspring: "))
    mut = int(input("Chance for a specimen to mutate: "))
    a = int(input("Parameter a: "))
    b = int(input("Parameter b: "))
    c = int(input("Parameter c: "))
    d = int(input("Parameter d: "))

    genetic(
        amount=amount,
        max_iterations=loops,
        stop_condition=cond,
        cross_chance=cross,
        mutation_chance=mut,
        a=a, b=b, c=c, d=d
    )


run()
