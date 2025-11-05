from collections import deque


class Node:
    
    def __init__(self, estado, pai=None, acao=None):
        self.estado = estado    
        self.pai = pai          
        self.acao = acao        
    
    def caminho(self):
        """Reconstrói a lista de AÇÕES que levam do início a este nó."""
        caminho_acoes = []
        no_atual = self
        while no_atual.pai is not None:
            caminho_acoes.append(no_atual.acao)
            no_atual = no_atual.pai
        
        return caminho_acoes[::-1]

def aplicar_acao(estado_atual, acao):
    """
    Função CHILD-NODE: Calcula o novo estado após aplicar uma AÇÃO.
    Estado: (local, estado_A, estado_B)
    """
    local, sala_a, sala_b = estado_atual
    
    if acao == 'Aspirar':
        if local == 'A':
            
            novo_estado = (local, 'L', sala_b)
        else: 
            
            novo_estado = (local, sala_a, 'L')
            
    elif acao == 'Mover_Direita':
        novo_estado = ('B', sala_a, sala_b)
        
    elif acao == 'Mover_Esquerda':
        novo_estado = ('A', sala_a, sala_b)
        
    else:
        return None 

    
    return novo_estado if novo_estado != estado_atual else None


def teste_objetivo(estado):
    """Verifica se todas as salas estão limpas."""
    
    return estado[1] == 'L' and estado[2] == 'L'    



def busca_aspirador_bfs(estado_inicial):
    
    
    ACOES = ['Aspirar', 'Mover_Direita', 'Mover_Esquerda']

    
    no_raiz = Node(estado_inicial)
    fronteira = deque([no_raiz])
    
    
    explorados = {estado_inicial}
    
    while fronteira:
        
        
        no_atual = fronteira.popleft() 
        
        
        if teste_objetivo(no_atual.estado):
            print(f"Objetivo alcançado no estado: {no_atual.estado}")
            return no_atual.caminho()
        
        
        for acao in ACOES:
            proximo_estado = aplicar_acao(no_atual.estado, acao)
            
            
            if proximo_estado and proximo_estado not in explorados:
                
                
                explorados.add(proximo_estado)
                
                
                no_filho = Node(estado=proximo_estado, pai=no_atual, acao=acao)
                
                
                fronteira.append(no_filho)
                
    return "Falha! Solução não encontrada."


ESTADO_INICIAL = ('B', 'S', 'L') 

print(f"Iniciando BFS a partir de {ESTADO_INICIAL}...")

solucao_acoes = busca_aspirador_bfs(ESTADO_INICIAL)

if isinstance(solucao_acoes, list):
    print("\n[Resultado Ótimo Encontrado (BFS)]")
    print(f"Número mínimo de ações: {len(solucao_acoes)}")
    print("Sequência de Ações:")
    for i, acao in enumerate(solucao_acoes):
        print(f"{i+1}. {acao}")
else:
    print(solucao_acoes)
