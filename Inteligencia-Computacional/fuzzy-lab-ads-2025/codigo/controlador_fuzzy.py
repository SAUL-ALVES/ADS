import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import os


if not os.path.exists('../imagens'):
    os.makedirs('../imagens')

print("=== INICIANDO SISTEMA FUZZY: AVALIAÇÃO DE QUALIDADE (TEMA B) ===")

# =============================================================================
# 1. DEFINIÇÃO DAS VARIÁVEIS LINGUÍSTICAS E UNIVERSOS DE DISCURSO
# =============================================================================

# Antecedentes (Entradas)
# Variabilidade: 0 a 1 (Índice de estabilidade da máquina)
variabilidade = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'variabilidade')

# Grau de Defeitos: 0 a 10 (Índice de severidade ou contagem)
defeitos = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'defeitos')

# Consequente (Saída)
# Qualidade Final: 0 a 10 (Nota final do produto)
qualidade = ctrl.Consequent(np.arange(0, 10.1, 0.1), 'qualidade')

# =============================================================================
# 2. CRIAÇÃO DAS FUNÇÕES DE PERTINÊNCIA
# =============================================================================

# Variabilidade (Baixa, Média, Alta)
variabilidade['baixa'] = fuzz.trimf(variabilidade.universe, [0, 0, 0.5])
variabilidade['media'] = fuzz.trimf(variabilidade.universe, [0, 0.5, 1])
variabilidade['alta']  = fuzz.trimf(variabilidade.universe, [0.5, 1, 1])

# Defeitos (Baixo, Médio, Alto)
defeitos['baixo'] = fuzz.trapmf(defeitos.universe, [0, 0, 2, 4])
defeitos['medio'] = fuzz.trimf(defeitos.universe, [2, 5, 8])
defeitos['alto']  = fuzz.trapmf(defeitos.universe, [6, 8, 10, 10])

# Qualidade (Reprovado, Atenção, Aprovado)
qualidade['reprovado'] = fuzz.trapmf(qualidade.universe, [0, 0, 3, 5])
qualidade['atencao']   = fuzz.trimf(qualidade.universe, [3, 5, 7])
qualidade['aprovado']  = fuzz.trapmf(qualidade.universe, [5, 7, 10, 10])

# Salvar gráficos das funções de pertinência
variabilidade.view()
plt.savefig('../imagens/pertinencia_variabilidade.png')
defeitos.view()
plt.savefig('../imagens/pertinencia_defeitos.png')
qualidade.view()
plt.savefig('../imagens/pertinencia_qualidade.png')

# =============================================================================
# 3. BASE DE REGRAS FUZZY
# =============================================================================

# Regra 1: Se Variabilidade Alta OU Defeitos Alto -> Reprovado
regra1 = ctrl.Rule(variabilidade['alta'] | defeitos['alto'], qualidade['reprovado'])

# Regra 2: Se Variabilidade Média E Defeitos Médio -> Atenção
regra2 = ctrl.Rule(variabilidade['media'] & defeitos['medio'], qualidade['atencao'])

# Regra 3: Se Variabilidade Baixa E Defeitos Baixo -> Aprovado
regra3 = ctrl.Rule(variabilidade['baixa'] & defeitos['baixo'], qualidade['aprovado'])

# Regra 4 (Refinamento): Se Variabilidade Baixa E Defeitos Médio -> Atenção
regra4 = ctrl.Rule(variabilidade['baixa'] & defeitos['medio'], qualidade['atencao'])

# Regra 5 (Refinamento): Se Variabilidade Média E Defeitos Baixo -> Aprovado
regra5 = ctrl.Rule(variabilidade['media'] & defeitos['baixo'], qualidade['aprovado'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5])
simulacao = ctrl.ControlSystemSimulation(sistema_controle)

# =============================================================================
# 4. TESTES DE CENÁRIOS (Inferência e Defuzzificação)
# =============================================================================

cenarios = [
    {'id': 1, 'nome': 'Cenário Ideal',    'var': 0.1, 'def': 1.0}, # Var Baixa, Def Baixo
    {'id': 2, 'nome': 'Cenário Crítico',  'var': 0.9, 'def': 9.0}, # Var Alta, Def Alto
    {'id': 3, 'nome': 'Fronteira/Médio',  'var': 0.5, 'def': 5.0}, # Var Média, Def Médio
    {'id': 4, 'nome': 'Var Alta/Def Baixo','var': 0.8, 'def': 1.5}, # Inconsistência (Máquina ruim, mas produto saiu ok)
    {'id': 5, 'nome': 'Var Baixa/Def Alto','var': 0.2, 'def': 8.5}  # Inconsistência (Máquina boa, mas defeito grave)
]

print(f"{'CENÁRIO':<20} | {'VAR':<5} | {'DEF':<5} | {'SAÍDA (0-10)':<12} | {'RESULTADO'}")
print("-" * 65)

for c in cenarios:
    simulacao.input['variabilidade'] = c['var']
    simulacao.input['defeitos'] = c['def']
    
    # Processa a inferência (Mamdani) e Defuzzificação (Centroide)
    simulacao.compute()
    
    resultado_valor = simulacao.output['qualidade']
    
    # Interpretação textual simples do resultado numérico
    if resultado_valor >= 6.0:
        status = "APROVADO"
    elif resultado_valor >= 4.0:
        status = "ATENÇÃO"
    else:
        status = "REPROVADO"
        
    print(f"{c['nome']:<20} | {c['var']:<5} | {c['def']:<5} | {resultado_valor:.2f}         | {status}")

    # Salvar gráfico do primeiro cenário como exemplo
    if c['id'] == 1:
        qualidade.view(sim=simulacao)
        plt.savefig('../imagens/saida_cenario_1.png')

print("\nImagens geradas e salvas na pasta 'imagens'.")