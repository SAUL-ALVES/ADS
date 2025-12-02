import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# --- 1. Definição das Variáveis (Antecedentes e Consequente) ---
# O universo de discurso para Comida e Serviço é de 0 a 10
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

# O universo de discurso para Gorjeta é de 0 a 25%
gorjeta = ctrl.Consequent(np.arange(0, 26, 1), 'gorjeta')

# --- 2. Criação das Funções de Pertinência (Fuzzificação) ---
# Comida: péssima, comível, deliciosa
comida['pessima'] = fuzz.trimf(comida.universe, [0, 0, 5])
comida['comivel'] = fuzz.trimf(comida.universe, [0, 5, 10])
comida['deliciosa'] = fuzz.trimf(comida.universe, [5, 10, 10])

# Serviço: ruim, aceitável, excelente
servico['ruim'] = fuzz.trimf(servico.universe, [0, 0, 5])
servico['aceitavel'] = fuzz.trimf(servico.universe, [0, 5, 10])
servico['excelente'] = fuzz.trimf(servico.universe, [5, 10, 10])

# Gorjeta: baixa, média, alta
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [0, 13, 25])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [13, 25, 25])

# --- 3. Base de Regras (Inferência) ---
# Regra 1: Se a comida é péssima OU o serviço é ruim, a gorjeta é baixa
regra1 = ctrl.Rule(comida['pessima'] | servico['ruim'], gorjeta['baixa'])

# Regra 2: Se o serviço é aceitável, a gorjeta é média
regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])

# Regra 3: Se a comida é deliciosa OU o serviço é excelente, a gorjeta é alta
regra3 = ctrl.Rule(comida['deliciosa'] | servico['excelente'], gorjeta['alta'])

# --- 4. Sistema de Controle e Simulação ---
sistema_gorjeta = ctrl.ControlSystem([regra1, regra2, regra3])
simulacao = ctrl.ControlSystemSimulation(sistema_gorjeta)

# --- 5. Entrada de Dados e Cálculo ---
print("\n--- Sistema Fuzzy de Gorjetas ---")
entrada_comida = float(input("Nota para a Comida (0-10): "))
entrada_servico = float(input("Nota para o Serviço (0-10): "))

simulacao.input['comida'] = entrada_comida
simulacao.input['servico'] = entrada_servico

# Computar o resultado (Defuzzificação)
simulacao.compute()

resultado_gorjeta = simulacao.output['gorjeta']

print(f"\nEntradas: Comida={entrada_comida}, Serviço={entrada_servico}")
print(f"Gorjeta sugerida: {resultado_gorjeta:.2f}%")

# --- 6. Visualização Gráfica ---
comida.view()
servico.view()
gorjeta.view(sim=simulacao)
plt.show()