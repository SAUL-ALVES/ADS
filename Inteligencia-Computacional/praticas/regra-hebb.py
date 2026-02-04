import numpy as np
import pandas as pd

# 1. Configuração das Entradas (Bipolar: -1 e 1)
# Tabela verdade para 3 variáveis (A, B, C)
inputs = np.array(
    [
        [-1, -1, -1],
        [-1, -1, 1],
        [-1, 1, -1],
        [-1, 1, 1],
        [1, -1, -1],
        [1, -1, 1],
        [1, 1, -1],
        [1, 1, 1],
    ]
)


# Função de Ativação (Degrau Bipolar) conforme slide 15
# Se yin >= 0, saída é 1. Caso contrário, -1.
def activation_function(yin):
    return np.where(yin >= 0, 1, -1)


# Algoritmo de Treinamento (Regra de Hebb) conforme slide 16
def train_hebb(inputs, targets):
    # Inicializar pesos e bias com 0 (Passo 1 do slide 16)
    weights = np.zeros(inputs.shape[1])
    bias = 0.0

    # Iterar sobre cada amostra (Passo 2 do slide 16)
    # Hebb simples geralmente é 'one-shot' (uma única época é suficiente para definir a direção)
    for i in range(len(inputs)):
        s = inputs[i]  # vetor de entrada s
        t = targets[i]  # saída desejada t

        # Passo 2.1: atualizar pesos -> w_novo = w_atual + s * t
        weights += s * t

        # Passo 2.2: atualizar bias -> b_novo = b_atual + t
        bias += t

    return weights, bias


# Função para testar e gerar a tabela de resultados
def test_and_report(inputs, weights, bias, targets, logic_name):
    y_in = np.dot(inputs, weights) + bias
    y_pred = activation_function(y_in)

    # Criando DataFrame para exibição bonita
    df = pd.DataFrame(inputs, columns=["A", "B", "C"])
    df["Target (t)"] = targets
    df["Y_in"] = y_in
    df["Predição (y)"] = y_pred
    df["Acertou?"] = df["Target (t)"] == df["Predição (y)"]

    print(f"\n--- Resultados para {logic_name} ---")
    print(f"Pesos Finais: {weights}")
    print(f"Bias Final: {bias}")
    print(df.to_string(index=False))

    # Análise de falha (importante para o relatório)
    if not df["Acertou?"].all():
        print(f"-> AVISO: A rede falhou em classificar corretamente {logic_name}.")
    else:
        print(f"-> SUCESSO: A rede aprendeu {logic_name} perfeitamente.")


# --- DEFINIÇÃO DOS TARGETS (Lógica Bipolar) ---

# Y1 = A AND B AND C
# Só é 1 (Verdadeiro) se todos forem 1.
targets_y1 = np.array([-1, -1, -1, -1, -1, -1, -1, 1])

# Y2 = A OR B OR C
# Só é -1 (Falso) se todos forem -1. O resto é 1.
targets_y2 = np.array([-1, 1, 1, 1, 1, 1, 1, 1])

# Y3 = (NOT(A AND B)) OR C
# Lógica: Se C for 1, saída é 1.
# Se C for -1, saída depende de NOT(A AND B).
# NOT(A AND B) só é Falso (-1) se A=1 e B=1.
# Logo, saída só é -1 se A=1, B=1 e C=-1.
targets_y3 = np.array([1, 1, 1, 1, 1, 1, -1, 1])

# --- EXECUÇÃO ---

# 1. Treinar e Testar AND
w1, b1 = train_hebb(inputs, targets_y1)
test_and_report(inputs, w1, b1, targets_y1, "Y1 (AND)")

# 2. Treinar e Testar OR
w2, b2 = train_hebb(inputs, targets_y2)
test_and_report(inputs, w2, b2, targets_y2, "Y2 (OR)")

# 3. Treinar e Testar Lógica Mista
w3, b3 = train_hebb(inputs, targets_y3)
test_and_report(inputs, w3, b3, targets_y3, "Y3 (NAND(AB) + C)")


"""
A implementação via código confirma que a Regra de Hebb (aprendizado não supervisionado/correlacional aplicado de forma supervisionada) encontra os pesos corretos de magnitude, mas não ajusta o limiar (bias) de forma fina o suficiente para garantir a separabilidade em funções onde as classes são desbalanceadas (como OR, onde há muito mais 1s do que -1s). Para corrigir isso, seria necessário usar a Regra Delta (Perceptron Learning Rule), que corrige erros baseada na diferença $(target - output)$.
"""
