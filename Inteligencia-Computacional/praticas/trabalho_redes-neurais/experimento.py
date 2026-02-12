import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron, SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.decomposition import PCA

# Configuração para reprodutibilidade básica
np.random.seed(42)

# 1. Carregamento e Pré-processamento
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Padronização (Obrigatório perante o enunciado)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Lista para armazenar resultados
results = {
    'Perceptron': {'accuracies': [], 'matrices': []},
    'ADALINE': {'accuracies': [], 'matrices': []},
    'MLP': {'accuracies': [], 'matrices': []}
}

# Número de execuções
n_runs = 10

print(f"Iniciando {n_runs} execuções independentes para cada modelo...\n")

# 2. Loop de Treinamento e Teste (Métricas)
for i in range(n_runs):
    # Divisão Treino/Teste (random_state=None para variar a cada loop)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, stratify=y
    )

    # --- Definição dos Modelos ---
    
    # Perceptron Clássico
    # max_iter definido para evitar loops infinitos em dados não separáveis
    perc = Perceptron(max_iter=100, eta0=0.1, random_state=i)
    
    # ADALINE (Simulado via SGDClassifier com perda quadrática)
    # loss='squared_error' minimiza o MSE (característica do Adaline)
    # learning_rate='constant' simula o passo fixo do Adaline clássico
    ada = SGDClassifier(loss='squared_error', learning_rate='constant', 
                        eta0=0.01, max_iter=1000, random_state=i)
    
    # MLP (Multilayer Perceptron)
    # 1 camada oculta com 10 neurônios, ativação ReLU
    mlp = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', 
                        solver='adam', max_iter=2000, random_state=i)

    models = {'Perceptron': perc, 'ADALINE': ada, 'MLP': mlp}

    for name, model in models.items():
        # Treino
        model.fit(X_train, y_train)
        
        # Teste
        y_pred = model.predict(X_test)
        
        # Métricas
        acc = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        
        results[name]['accuracies'].append(acc)
        results[name]['matrices'].append(cm)

# 3. Apresentação dos Resultados Quantitativos
print("--- RESULTADOS AGREGADOS (10 Execuções) ---\n")

for name in results:
    accs = results[name]['accuracies']
    mean_acc = np.mean(accs)
    std_acc = np.std(accs)
    
    print(f"MODELO: {name}")
    print(f"Acurácia Média: {mean_acc:.2%}")
    print(f"Desvio Padrão:  {std_acc:.4f}")
    
    # Soma das matrizes de confusão para ter uma visão geral dos erros
    sum_cm = np.sum(results[name]['matrices'], axis=0)
    print("Matriz de Confusão Acumulada:")
    print(sum_cm)
    print("-" * 30)

# 4. Visualização das Fronteiras de Decisão (Usando PCA para 2D)
print("\nGerando gráficos de fronteiras de decisão (via PCA)...")

# Redução de dimensionalidade para visualização (justificado no relatório)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Treinar novos modelos apenas nos dados 2D para visualização
# Nota: Usamos todo o dataset aqui para visualizar a fronteira "final" aprendida
X_viz_train, X_viz_test, y_viz_train, y_viz_test = train_test_split(
    X_pca, y, test_size=0.3, stratify=y, random_state=42
)

models_viz = {
    'Perceptron': Perceptron(max_iter=100, eta0=0.1, random_state=42),
    'ADALINE': SGDClassifier(loss='squared_error', learning_rate='constant', 
                             eta0=0.01, max_iter=1000, random_state=42),
    'MLP': MLPClassifier(hidden_layer_sizes=(10,), activation='relu', 
                         solver='adam', max_iter=2000, random_state=42)
}

# Configuração da grade de plotagem
h = .02  # tamanho do passo na malha
x_min, x_max = X_pca[:, 0].min() - 1, X_pca[:, 0].max() + 1
y_min, y_max = X_pca[:, 1].min() - 1, X_pca[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

plt.figure(figsize=(18, 5))

for idx, (name, model) in enumerate(models_viz.items()):
    # Treinar no espaço 2D
    model.fit(X_viz_train, y_viz_train)
    
    # Predizer na malha
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    ax = plt.subplot(1, 3, idx + 1)
    
    # Plotar contornos
    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    
    # Plotar pontos de dados (Teste e Treino juntos para ver distribuição total)
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
    
    ax.set_title(f"{name}\n(Fronteiras de Decisão - PCA)")
    ax.set_xlabel('Componente Principal 1')
    ax.set_ylabel('Componente Principal 2')

# Legenda
plt.legend(handles=scatter.legend_elements()[0], labels=target_names.tolist(), loc="upper right")
plt.tight_layout()
plt.show()

print("Concluído.")