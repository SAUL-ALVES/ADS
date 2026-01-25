import random
import numpy as np
import matplotlib.pyplot as plt

# --- Configurações ---
N_QUEENS = 8  # Tamanho do tabuleiro (N)
POP_SIZE = 100
GEN_MAX = 500
MUTATION_RATE = 0.05
CROSSOVER_RATE = 0.8

def create_individual():
    """Cria um indivíduo: vetor de tamanho N com valores 0 a N-1."""
    return [random.randint(0, N_QUEENS - 1) for _ in range(N_QUEENS)]

def calculate_conflicts(individual):
    """Conta o número de pares de rainhas se atacando (diagonais e linhas)."""
    conflicts = 0
    n = len(individual)
    
    # Conflitos de linha (valores repetidos)
    # Nota: A representação sugere que conflitos de coluna são impossíveis,
    # mas se usarmos randint sem permutação, conflitos de linha são possíveis.
    # O prompt diz: "valor armazenado representa a linha".
    for i in range(n):
        for j in range(i + 1, n):
            # Mesma linha
            if individual[i] == individual[j]:
                conflicts += 1
            # Mesma diagonal
            elif abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def fitness(individual):
    """Maximizar: 1 / (1 + conflitos). Ótimo = 1.0"""
    return 1.0 / (1.0 + calculate_conflicts(individual))

def crossover(p1, p2):
    """Cruzamento de Ponto Único."""
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, N_QUEENS - 2)
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]
        return c1, c2
    return p1[:], p2[:]

def mutate(individual):
    """Mutação: altera a linha de uma rainha aleatória."""
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, N_QUEENS - 1)
        individual[idx] = random.randint(0, N_QUEENS - 1)
    return individual

def tournament_selection(population, scores, k=3):
    """Seleção por Torneio."""
    selection_ix = random.randint(0, len(population)-1)
    for ix in [random.randint(0, len(population)-1) for _ in range(k-1)]:
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return population[selection_ix]

# --- Execução Principal ---
population = [create_individual() for _ in range(POP_SIZE)]
best_fitness_history = []

for gen in range(GEN_MAX):
    scores = [fitness(ind) for ind in population]
    
    # Melhor da geração
    best_score = max(scores)
    best_fitness_history.append(best_score)
    
    if best_score == 1.0:
        print(f"Solução encontrada na geração {gen}!")
        best_ind = population[scores.index(best_score)]
        print(f"Indivíduo: {best_ind}")
        break

    # Nova população
    new_pop = []
    # Elitismo: mantém o melhor
    best_idx = scores.index(best_score)
    new_pop.append(population[best_idx])
    
    while len(new_pop) < POP_SIZE:
        p1 = tournament_selection(population, scores)
        p2 = tournament_selection(population, scores)
        c1, c2 = crossover(p1, p2)
        new_pop.append(mutate(c1))
        if len(new_pop) < POP_SIZE:
            new_pop.append(mutate(c2))
    
    population = new_pop

# Plotagem simples para análise
plt.plot(best_fitness_history)
plt.title('Convergência N-Rainhas')
plt.xlabel('Geração')
plt.ylabel('Melhor Fitness')
plt.show()