# Este é um exemplo conceitual de como a formulação seria estruturada.
# O mapa completo da Romênia (distâncias e vizinhos) seria necessário
# para uma implementação funcional.

#____________________________LETRA A)_______________________________
class TwoFriendsProblem:
    def __init__(self, romania_map, initial_state):
        """
        romania_map: Um dicionário de dicionários representando o grafo.
                     ex: {'Arad': {'Zerind': 75, 'Sibiu': 140, ...}, ...}
        initial_state: Uma tupla (amigo1_cidade, amigo2_cidade)
        """
        self.romania_map = romania_map
        self.initial_state = initial_state
        print(f"Problema iniciado com o estado: {initial_state}")

    def get_initial_state(self):
        return self.initial_state

    def is_goal_state(self, state):
        """O objetivo é alcançado se ambos estiverem na mesma cidade."""
        return state[0] == state[1]

    def get_actions(self, state):
        """Retorna todas as ações possíveis (pares de movimentos)."""
        city1, city2 = state
        neighbors1 = self.romania_map.get(city1, {}).keys()
        neighbors2 = self.romania_map.get(city2, {}).keys()
        
        
        actions = []
        for next1 in neighbors1:
            for next2 in neighbors2:
                actions.append((next1, next2))
        return actions

    def get_result(self, state, action):
        """O resultado da ação é simplesmente o novo estado (nova_cidade1, nova_cidade2)."""
        return action 

    def get_step_cost(self, state_from, action_to):
        """
        O custo é o máximo do tempo de viagem de cada amigo.
        O tempo é igual à distância da estrada.
        """
        city1_from, city2_from = state_from
        city1_to, city2_to = action_to
        
        cost1 = self.romania_map[city1_from][city1_to]
        cost2 = self.romania_map[city2_from][city2_to]
        
        return max(cost1, cost2)


simple_map = {
    'Arad': {'Sibiu': 140},
    'Sibiu': {'Arad': 140, 'Fagaras': 99},
    'Fagaras': {'Sibiu': 99}
}


problem = TwoFriendsProblem(simple_map, ('Arad', 'Fagaras'))
print(f"Estado inicial é objetivo? {problem.is_goal_state(problem.get_initial_state())}")


state = ('Arad', 'Fagaras')
actions = problem.get_actions(state)
print(f"Ações de {state}: {actions}")


action = actions[0] 
cost = problem.get_step_cost(state, action)
result = problem.get_result(state, action)

print(f"Ação: {action}, Custo: {cost} (max(d(Arad,Sibiu), d(Fagaras,Sibiu)) = max(140, 99))")
print(f"Estado resultante: {result}")
print(f"Novo estado é objetivo? {problem.is_goal_state(result)}")



#____________________________LETRA B)_______________________________
def straight_line_dist(city1, city2):
    """
    Função hipotética que retorna a distância em linha reta (D(i,j)).
    Em um problema real, isso viria de uma tabela de consulta.
    Vamos simular alguns valores.
    """
    distances = {
        ('Arad', 'Bucharest'): 366,
        ('Arad', 'Fagaras'): 176,
        ('Fagaras', 'Bucharest'): 178,
    }
    
    val = distances.get((city1, city2))
    if val is None:
        val = distances.get((city2, city1))
    return val if val is not None else 0

def admissible_heuristic(state):
    """
    Implementa a heurística admissível h(n) = D(i, j) / 2.
    O estado 'n' é a tupla (cidade_amigo1, cidade_amigo2).
    """
    city1, city2 = state
    
    
    if city1 == city2:
        return 0
        
    D_i_j = straight_line_dist(city1, city2)
    
    
    return D_i_j / 2


state1 = ('Arad', 'Bucharest')
h1 = admissible_heuristic(state1)
print(f"Heurística para {state1}: D({state1[0]},{state1[1]})/2 = {straight_line_dist(state1[0], state1[1])}/2 = {h1}")

state2 = ('Arad', 'Fagaras')
h2 = admissible_heuristic(state2)
print(f"Heurística para {state2}: D({state2[0]},{state2[1]})/2 = {straight_line_dist(state2[0], state2[1])}/2 = {h2}")

#____________________________LETRA C)_______________________________


bipartite_map = {
    'A': {'B': 10},
    'B': {'A': 10, 'C': 20},
    'C': {'B': 20}
}


state = ('A', 'B')
print(f"--- Caso 1: Começando em {state} (U, V) ---")


state_t1 = ('B', 'A')
print(f"Depois do Turno 1, um estado possível é {state_t1} (V, U)")

state_t2 = ('B', 'C') 
print(f"Depois do Turno 1, outro estado possível é {state_t2} (V, U)")

print("Em ambos os casos, eles ainda estão em cores/conjuntos diferentes. Eles nunca se encontrarão.")


state = ('A', 'C')
print(f"\n--- Caso 2: Começando em {state} (U, U) ---")

next_state = ('B', 'B')
print(f"Ação (A->B, C->B) leva ao estado {next_state}")
print(f"Eles se encontram! Solução existe.")

#____________________________LETRA D)_______________________________

def trace_solution_with_repeat():
    print("Demonstração de uma solução que exige revisita.")
    
    
    path_friend_1 = ['A', 'C', 'D', 'C', 'D']
    path_friend_2 = ['B', 'E', 'F', 'G', 'D']
    
    total_time = 0
    
   
    
    current_state = (path_friend_1[0], path_friend_2[0])
    print(f"Turno 0 (Início): Estado = {current_state}, Tempo = {total_time}")
    
    for i in range(1, len(path_friend_1)):
        move_cost = 10 
        total_time += move_cost
        
        current_state = (path_friend_1[i], path_friend_2[i])
        
        print(f"Turno {i}:")
        print(f"  Amigo 1: {path_friend_1[i-1]} -> {path_friend_1[i]}")
        print(f"  Amigo 2: {path_friend_2[i-1]} -> {path_friend_2[i]}")
        print(f"  Estado = {current_state}, Tempo Total = {total_time}")

    
    cities_visited_by_1 = set()
    has_repeat = False
    for city in path_friend_1:
        if city in cities_visited_by_1:
            print(f"\nAmigo 1 visitou {city} duas vezes!")
            has_repeat = True
        cities_visited_by_1.add(city)
        
    if current_state[0] == current_state[1]:
        print("Objetivo alcançado.")

trace_solution_with_repeat()