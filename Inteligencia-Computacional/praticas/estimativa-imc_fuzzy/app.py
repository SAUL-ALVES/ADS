import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import warnings
import pandas as pd

warnings.filterwarnings("ignore")

peso = ctrl.Antecedent(np.arange(40, 151, 1), 'peso')
altura = ctrl.Antecedent(np.arange(1.5, 2.01, 0.01), 'altura')
imc = ctrl.Consequent(np.arange(15, 46, 1), 'imc', defuzzify_method='centroid')

peso['leve']  = fuzz.trapmf(peso.universe,  [40, 40, 60, 75])
peso['medio'] = fuzz.trimf(peso.universe,   [70, 85, 100])
peso['alto']  = fuzz.trapmf(peso.universe,  [95, 110, 150, 150])

altura['baixa'] = fuzz.trapmf(altura.universe, [1.5, 1.5, 1.6, 1.7])
altura['media'] = fuzz.trimf(altura.universe,  [1.65, 1.75, 1.85])
altura['alta']  = fuzz.trapmf(altura.universe, [1.8, 1.9, 2.0, 2.0])

imc['muito_magro'] = fuzz.trimf(imc.universe, [15, 16, 18.5])
imc['saudavel']    = fuzz.trimf(imc.universe, [18.5, 23, 25])
imc['sobrepeso']   = fuzz.trimf(imc.universe, [25, 28, 30])
imc['obeso']       = fuzz.trapmf(imc.universe, [29, 35, 45, 45])

print(peso.universe)
print(altura.universe)
print(imc.universe)

print(len(peso.universe))
print(len(altura.universe))
print(len(imc.universe))

print(peso.terms)
print(altura.terms)
print(imc.terms)

print(peso['leve'].mf)
print(altura['media'].mf)
print(imc['obeso'].mf)

peso.view()
altura.view()
imc.view()

regra1  = ctrl.Rule(peso['leve']  & altura['baixa'], imc['muito_magro'])
regra2  = ctrl.Rule(peso['leve']  & altura['media'], imc['muito_magro'])
regra3  = ctrl.Rule(peso['leve']  & altura['alta'],  imc['muito_magro'])

regra4  = ctrl.Rule(peso['medio'] & altura['media'], imc['saudavel'])
regra5  = ctrl.Rule(peso['medio'] & altura['baixa'], imc['saudavel'])
regra6  = ctrl.Rule(peso['medio'] & altura['alta'],  imc['saudavel'])

regra7  = ctrl.Rule(peso['alto'] & altura['baixa'], imc['sobrepeso'])
regra8  = ctrl.Rule(peso['alto'] & altura['media'], imc['sobrepeso'])
regra9  = ctrl.Rule(peso['alto'] & altura['alta'],  imc['obeso'])

regra10 = ctrl.Rule(peso['medio'] & altura['baixa'], imc['sobrepeso'])
regra11 = ctrl.Rule(peso['medio'] & altura['alta'],  imc['sobrepeso'])

sistema_controle = ctrl.ControlSystem([
    regra1, regra2, regra3, regra4, regra5,
    regra6, regra7, regra8, regra9,
    regra10, regra11
])

simulador_imc = ctrl.ControlSystemSimulation(sistema_controle)

NUM_PONTOS = 100

np.random.seed(42)
dataset_peso   = np.clip(np.random.normal(80, 15, NUM_PONTOS), 40, 150)
dataset_altura = np.clip(np.random.normal(1.75, 0.1, NUM_PONTOS), 1.5, 2.0)

dataset_imc_classico = dataset_peso / (dataset_altura ** 2)

dataset_imc_fuzzy = []

for p, a in zip(dataset_peso, dataset_altura):
    try:
        simulador_imc.input['peso'] = p
        simulador_imc.input['altura'] = a
        simulador_imc.compute()
        dataset_imc_fuzzy.append(simulador_imc.output['imc'])
    except:
        dataset_imc_fuzzy.append(np.nan)

dataset_imc_fuzzy = np.array(dataset_imc_fuzzy)

valid = ~np.isnan(dataset_imc_fuzzy)
imc_classico_valid = dataset_imc_classico[valid]
imc_fuzzy_valid    = dataset_imc_fuzzy[valid]

correlacao = np.corrcoef(imc_classico_valid, imc_fuzzy_valid)[0, 1]
print(f"Correlação: {correlacao:.4f}")

erro_absoluto = np.abs(imc_classico_valid - imc_fuzzy_valid)
print(f"Erro absoluto médio: {erro_absoluto.mean():.4f}")
print(f"Erro absoluto máximo: {erro_absoluto.max():.4f}")
print(f"Erro absoluto mínimo: {erro_absoluto.min():.4f}")

plt.figure(figsize=(8, 6))
plt.scatter(imc_classico_valid, imc_fuzzy_valid)
plt.plot([15,45], [15,45], 'r--')
plt.xlabel("IMC Clássico")
plt.ylabel("IMC Fuzzy")
plt.title("Comparação entre IMC Clássico e IMC Fuzzy")
plt.show()

def testar(peso_val, altura_val):
    simulador_imc.input['peso'] = peso_val
    simulador_imc.input['altura'] = altura_val
    simulador_imc.compute()

    imc_class = peso_val / (altura_val ** 2)
    imc_fuzzy = simulador_imc.output['imc']

    print(f"\nPeso={peso_val}kg Altura={altura_val}m")
    print(f"IMC clássico: {imc_class:.2f}")
    print(f"IMC fuzzy:    {imc_fuzzy:.2f}")

    imc.view(sim=simulador_imc)
    plt.show()
    
testar(65, 1.75)   