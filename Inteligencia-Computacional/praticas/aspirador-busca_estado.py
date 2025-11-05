from collections import deque

def modelo_de_transicao(estado, acao):
    local, (status_A, status_B) = estado
    
    if acao == 'ASPIRAR':
        if local == 'A':
            return ('A', ('Limpo', status_B))
        else:
            return ('B', (status_A, 'Limpo'))
            
    elif acao == 'ESQUERDA':
        if local == 'B':
            return ('A', (status_A, status_B))
        else:
            return estado
            
    elif acao == 'DIREITA':
        if local == 'A':
            return ('B', (status_A, status_B))
        else:
            return estado

def teste_de_objetivo(estado):
    local, (status_A, status_B) = estado
    return status_A == 'Limpo' and status_B == 'Limpo'

def acoes_possiveis(estado):
    return ['ESQUERDA', 'DIREITA', 'ASPIRAR']

class No:
    def __init__(self, estado, pai=None, acao=None, custo_caminho=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo_caminho = custo_caminho

    def __repr__(self):
        return f"<Nó {self.estado}>"

def busca_em_largura(estado_inicial):
    no_inicial = No(estado=estado_inicial, custo_caminho=0)
    
    if teste_de_objetivo(no_inicial.estado):
        return formatar_solucao(no_inicial)

    fronteira = deque([no_inicial])
    
    explorados = set()
    explorados.add(estado_inicial)

    while True:
        if not fronteira:
            return None

        no_atual = fronteira.popleft()

        for acao in acoes_possiveis(no_atual.estado):
            novo_estado = modelo_de_transicao(no_atual.estado, acao)
            
            novo_custo = no_atual.custo_caminho + 1
            no_filho = No(estado=novo_estado, 
                          pai=no_atual, 
                          acao=acao, 
                          custo_caminho=novo_custo)

            if novo_estado not in explorados:
                if teste_de_objetivo(novo_estado):
                    return formatar_solucao(no_filho)
                
                fronteira.append(no_filho)
                explorados.add(novo_estado)

def formatar_solucao(no):
    caminho = []
    custo_total = no.custo_caminho
    while no.pai is not None:
        caminho.append((no.acao, no.estado))
        no = no.pai
    
    caminho.append(("Início", no.estado))
    caminho.reverse()
    
    return caminho, custo_total

estado_inicial_exemplo = ('A', ('Sujo', 'Sujo'))

print(f"Buscando solução a partir de: {estado_inicial_exemplo}...")

solucao, custo = busca_em_largura(estado_inicial_exemplo)

if solucao:
    print(f"\nSolução encontrada! Custo total: {custo}")
    for passo in solucao:
        acao, estado = passo
        print(f"  - Ação: {acao:<10} -> Estado: {estado}")
else:
    print("Falha: Não foi possível encontrar uma solução.")