import numpy as np
import matplotlib.pyplot as plt
import copy

class AlgoritmoGenetico:
    def __init__(self, elitismo_pct, taxa_mutacao=0.01, pop_size=100, n_geracoes=50, n_bits=20):
        self.pop_size = pop_size
        self.n_bits = n_bits
        self.n_geracoes = n_geracoes
        self.elitismo_count = int(pop_size * elitismo_pct)
        self.taxa_mutacao = taxa_mutacao
        
        # Limites do problema
        self.x_min = -10
        self.x_max = 10
        
        # Histórico para gráficos
        self.history_best_fitness = []
        self.history_avg_fitness = []
        self.history_diversity = []

    def decode(self, cromossomo):
        # Converte lista de bits para inteiro
        chars = ''.join(map(str, cromossomo))
        inteiro = int(chars, 2)
        # Mapeia para [-10, 10]
        precisao = (self.x_max - self.x_min) / (2**self.n_bits - 1)
        return self.x_min + (inteiro * precisao)

    def fitness_function(self, x):
        # Queremos minimizar f(x) = 2x^2 + 5x.
        # AGs geralmente maximizam. Podemos minimizar transformando o problema:
        # Fitness = - (2x^2 + 5x) OU Fitness = 1 / (f(x) + constante)
        # Aqui usaremos negativo direto para facilitar a leitura dos gráficos (quanto menor, melhor)
        return 2*(x**2) + 5*x

    def calcular_diversidade(self, populacao):
        # Distância de Hamming média em relação ao melhor indivíduo ou centroide
        # Método simplificado: Distância média par a par é custoso O(N^2).
        # Usaremos: Variância média dos bits (0.5 = diversidade máx, 0.0 = todos iguais)
        pop_matrix = np.array(populacao)
        variancias = np.var(pop_matrix, axis=0)
        return np.mean(variancias)

    def inicializar_populacao(self):
        return [np.random.randint(0, 2, self.n_bits).tolist() for _ in range(self.pop_size)]

    def torneio(self, populacao, fitnesses):
        # Torneio binário
        i1, i2 = np.random.choice(len(populacao), 2, replace=False)
        # Nota: Como queremos MINIMIZAR a função original, vence quem tem MENOR valor
        if fitnesses[i1] < fitnesses[i2]:
            return populacao[i1]
        return populacao[i2]

    def crossover(self, pai1, pai2):
        if np.random.rand() < 0.9: # Taxa de crossover fixa alta
            ponto = np.random.randint(1, self.n_bits)
            filho1 = pai1[:ponto] + pai2[ponto:]
            filho2 = pai2[:ponto] + pai1[ponto:]
            return filho1, filho2
        return pai1, pai2

    def mutacao(self, individuo):
        novo_ind = []
        for bit in individuo:
            if np.random.rand() < self.taxa_mutacao:
                novo_ind.append(1 - bit) # Inverte o bit
            else:
                novo_ind.append(bit)
        return novo_ind

    def executar(self):
        populacao = self.inicializar_populacao()
        
        for g in range(self.n_geracoes):
            # 1. Avaliação (Decodificar e Calcular f(x))
            valores_x = [self.decode(ind) for ind in populacao]
            fitnesses = [self.fitness_function(x) for x in valores_x]
            
            # Registrar métricas
            best_val = np.min(fitnesses) # Menor valor é o melhor
            avg_val = np.mean(fitnesses)
            diversidade = self.calcular_diversidade(populacao)
            
            if diversidade < 0.05:
                self.taxa_mutacao = 0.10  # Aumenta mutação para 10% (choque)
            elif diversidade < 0.10:
                self.taxa_mutacao = 0.05  # Aumenta para 5%
            else:
                self.taxa_mutacao = 0.01
            
            self.history_best_fitness.append(best_val)
            self.history_avg_fitness.append(avg_val)
            self.history_diversity.append(diversidade)
            
            # 2. Elitismo
            # Ordenar população pelo fitness (menor para maior)
            indices_ordenados = np.argsort(fitnesses)
            populacao_ordenada = [populacao[i] for i in indices_ordenados]
            
            nova_populacao = []
            
            # Preservar elite
            if self.elitismo_count > 0:
                nova_populacao.extend(populacao_ordenada[:self.elitismo_count])
            
            # 3. Gerar o resto da população
            while len(nova_populacao) < self.pop_size:
                p1 = self.torneio(populacao, fitnesses)
                p2 = self.torneio(populacao, fitnesses)
                
                f1, f2 = self.crossover(p1, p2)
                
                f1 = self.mutacao(f1)
                f2 = self.mutacao(f2)
                
                nova_populacao.append(f1)
                if len(nova_populacao) < self.pop_size:
                    nova_populacao.append(f2)
            
            populacao = nova_populacao

        return self.decode(populacao_ordenada[0]), self.fitness_function(self.decode(populacao_ordenada[0]))

# --- Execução dos Experimentos ---

configs = [
    {"nome": "A (0% Elitismo)", "elitismo": 0.0},
    {"nome": "B (2% Elitismo)", "elitismo": 0.02},
    {"nome": "C (20% Elitismo)", "elitismo": 0.20}
]

resultados = {}

print(f"Mínimo Teórico: x = -1.25, f(x) = -3.125\n")

plt.figure(figsize=(15, 5))

# Para plotar a média das 5 execuções
cores = ['r', 'g', 'b']

for i, conf in enumerate(configs):
    print(f"--- Rodando Experimento {conf['nome']} ---")
    
    # Acumuladores para média das execuções
    soma_best = np.zeros(50) # assumindo 50 gerações
    soma_div = np.zeros(50)
    melhor_solucao_global = float('inf')
    
    for run in range(5): # 5 Execuções
        ag = AlgoritmoGenetico(elitismo_pct=conf['elitismo'], n_geracoes=50)
        melhor_x, melhor_fit = ag.executar()
        
        soma_best += np.array(ag.history_best_fitness)
        soma_div += np.array(ag.history_diversity)
        
        if melhor_fit < melhor_solucao_global:
            melhor_solucao_global = melhor_fit
            
    # Médias
    media_best = soma_best / 5
    media_div = soma_div / 5
    
    # Plot Fitness
    plt.subplot(1, 2, 1)
    plt.plot(media_best, label=conf['nome'], color=cores[i])
    plt.title("Convergência (Melhor Fitness Médio)")
    plt.xlabel("Geração")
    plt.ylabel("f(x) Min")
    plt.grid(True)
    
    # Plot Diversidade
    plt.subplot(1, 2, 2)
    plt.plot(media_div, label=conf['nome'], color=cores[i], linestyle='--')
    plt.title("Diversidade Populacional")
    plt.xlabel("Geração")
    plt.ylabel("Variância de Bits")
    plt.grid(True)

    print(f"Melhor resultado encontrado em 5 execuções: {melhor_solucao_global:.5f}")

plt.subplot(1, 2, 1)
plt.legend()
plt.subplot(1, 2, 2)
plt.legend()
plt.tight_layout()
plt.show()