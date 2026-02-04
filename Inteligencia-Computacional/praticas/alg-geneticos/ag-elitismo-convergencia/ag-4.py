import numpy as np
import matplotlib.pyplot as plt

class AlgoritmoGeneticoBase:
    def __init__(self, elitismo_pct, adaptativo=False, pop_size=100, n_geracoes=50, n_bits=20):
        self.pop_size = pop_size
        self.n_bits = n_bits
        self.n_geracoes = n_geracoes
        self.elitismo_count = int(pop_size * elitismo_pct)
        self.adaptativo = adaptativo
        self.taxa_mutacao_base = 0.01
        
        # Limites
        self.x_min = -10
        self.x_max = 10
        
        # Histórico
        self.history_best = []
        self.history_div = []

    def decode(self, cromossomo):
        chars = ''.join(map(str, cromossomo))
        inteiro = int(chars, 2)
        precisao = (self.x_max - self.x_min) / (2**self.n_bits - 1)
        return self.x_min + (inteiro * precisao)

    def fitness(self, x):
        # f(x) = 2x^2 + 5x
        return 2*(x**2) + 5*x

    def calc_diversidade(self, pop):
        return np.mean(np.var(pop, axis=0))

    def executar(self):
        pop = [np.random.randint(0, 2, self.n_bits).tolist() for _ in range(self.pop_size)]
        
        for g in range(self.n_geracoes):
            # 1. Avaliar
            vals = [self.decode(ind) for ind in pop]
            fits = [self.fitness(x) for x in vals]
            
            div = self.calc_diversidade(pop)
            self.history_best.append(np.min(fits))
            self.history_div.append(div)
            
            # --- LÓGICA ADAPTATIVA (PARTE 4) ---
            if self.adaptativo:
                # Se a diversidade está muito baixa, CHUTE na mutação
                if div < 0.05:
                    taxa_atual = 0.20  # 20% de mutação (Explosão)
                elif div < 0.10:
                    taxa_atual = 0.05  # 5% de mutação
                else:
                    taxa_atual = 0.01  # 1% Normal
            else:
                taxa_atual = self.taxa_mutacao_base

            # 2. Elitismo
            indices = np.argsort(fits)
            pop_sorted = [pop[i] for i in indices]
            nova_pop = pop_sorted[:self.elitismo_count]
            
            # 3. Cruzamento e Mutação
            while len(nova_pop) < self.pop_size:
                # Torneio simples
                i1, i2 = np.random.choice(self.pop_size, 2, replace=False)
                p1 = pop[i1] if fits[i1] < fits[i2] else pop[i2]
                
                i3, i4 = np.random.choice(self.pop_size, 2, replace=False)
                p2 = pop[i3] if fits[i3] < fits[i4] else pop[i4]
                
                # Crossover
                if np.random.rand() < 0.9:
                    pt = np.random.randint(1, self.n_bits)
                    f1 = p1[:pt] + p2[pt:]
                else:
                    f1 = p1[:]
                
                # Mutação (usando a taxa dinâmica definida acima)
                f1_mut = []
                for bit in f1:
                    if np.random.rand() < taxa_atual:
                        f1_mut.append(1 - bit)
                    else:
                        f1_mut.append(bit)
                
                nova_pop.append(f1_mut)
            
            pop = nova_pop
            
        return np.min(self.history_best)

# --- Executando a Comparação ---

print("Rodando Comparação Parte 4...")

# Configurações
# C Original: 20% Elitismo, Sem adaptação
# C Adaptativo: 20% Elitismo, Com adaptação
experimentos = [
    {"nome": "C (Original)", "adapt": False, "cor": "blue"},
    {"nome": "C (Adaptativo)", "adapt": True, "cor": "orange"}
]

plt.figure(figsize=(12, 5))

for exp in experimentos:
    soma_best = np.zeros(50)
    soma_div = np.zeros(50)
    
    # Média de 10 execuções para suavizar curvas
    for _ in range(10):
        ag = AlgoritmoGeneticoBase(elitismo_pct=0.20, adaptativo=exp["adapt"], n_geracoes=50)
        ag.executar()
        soma_best += np.array(ag.history_best)
        soma_div += np.array(ag.history_div)
        
    avg_best = soma_best / 10
    avg_div = soma_div / 10
    
    # Plot Fitness
    plt.subplot(1, 2, 1)
    plt.plot(avg_best, label=exp["nome"], color=exp["cor"])
    
    # Plot Diversidade
    plt.subplot(1, 2, 2)
    plt.plot(avg_div, label=exp["nome"], color=exp["cor"], linestyle="--" if exp["adapt"] else "-")

# Configuração visual
plt.subplot(1, 2, 1)
plt.title("Comparação de Convergência")
plt.xlabel("Geração")
plt.ylabel("Melhor Fitness")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.title("Comparação de Diversidade")
plt.xlabel("Geração")
plt.ylabel("Variância (Diversidade)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()