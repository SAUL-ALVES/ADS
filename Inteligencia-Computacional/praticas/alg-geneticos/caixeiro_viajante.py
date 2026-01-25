import random
import numpy as np
import matplotlib.pyplot as plt

# --- Configurações ---
NUM_CITIES = 20
POP_SIZE = 100
GEN_MAX = 500
MUTATION_RATE = 0.1  # Taxa um pouco maior para evitar ótimo local
CROSSOVER_RATE = 0.9

# Gerar cidades aleatórias (coordenadas x, y)
cities = np.random.rand(NUM_CITIES, 2) * 100

def create_individual():
    """Cria uma permutação aleatória das cidades."""
    ind = list(range(NUM_CITIES))
    random.shuffle(ind)
    return ind

def calculate_distance(individual):
    dist = 0
    for i in range(len(individual)):
        city_a = cities[individual[i]]
        # Conecta a última cidade à primeira para fechar o ciclo
        city_b = cities[individual[(i + 1) % len(individual)]]
        dist += np.linalg.norm(city_a - city_b)
    return dist

def fitness(individual):
    """Maximizar: 1 / distância total."""
    dist = calculate_distance(individual)
    if dist == 0: return float('inf')
    return 1.0 / dist

def order_crossover(p1, p2):
    """Order Crossover (OX) para preservar permutação."""
    if random.random() > CROSSOVER_RATE:
        return p1[:], p2[:]
    
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    
    def apply_ox(parent1, parent2):
        child = [-1] * size
        # Copia o subsegmento do pai 1
        child[start:end] = parent1[start:end]
        # Preenche o resto com genes do pai 2 na ordem que aparecem
        p2_genes = [item for item in parent2 if item not in child]
        current_p2 = 0
        for i in range(size):
            if child[i] == -1:
                child[i] = p2_genes[current_p2]
                current_p2 += 1
        return child

    c1 = apply_ox(p1, p2)
    c2 = apply_ox(p2, p1)
    return c1, c2

def mutate_swap(individual):
    """Mutação por troca (Swap) para manter permutação."""
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def tournament_selection(population, scores, k=4):
    selection_ix = random.randint(0, len(population)-1)
    for ix in [random.randint(0, len(population)-1) for _ in range(k-1)]:
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

# --- Execução Principal ---
population = [create_individual() for _ in range(POP_SIZE)]
history_dist = []

for gen in range(GEN_MAX):
    # Calcula aptidão (fitness) e distâncias reais
    dists = [calculate_distance(ind) for ind in population]
    scores = [1.0/d for d in dists]
    
    best_dist = min(dists)
    history_dist.append(best_dist)
    
    # Nova população com Elitismo
    new_pop = []
    best_idx = dists.index(best_dist)
    new_pop.append(population[best_idx]) # Mantém o melhor
    
    while len(new_pop) < POP_SIZE:
        p1 = tournament_selection(population, scores)
        p2 = tournament_selection(population, scores)
        c1, c2 = order_crossover(p1, p2)
        new_pop.append(mutate_swap(c1))
        if len(new_pop) < POP_SIZE:
            new_pop.append(mutate_swap(c2))
            
    population = new_pop

print(f"Melhor distância final: {min(dists):.2f}")

# Plotagem
plt.plot(history_dist)
plt.title('Otimização TSP (Distância)')
plt.xlabel('Geração')
plt.ylabel('Distância Total (Menor é melhor)')
plt.show()