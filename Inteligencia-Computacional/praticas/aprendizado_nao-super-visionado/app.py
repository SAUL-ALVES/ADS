import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from scipy.stats import mode
import warnings
warnings.filterwarnings('ignore')

# 1. Preparação dos Dados
iris = load_iris()
# Criando o DataFrame sem os rótulos
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y_true = iris.target # Guardando os rótulos reais apenas para a etapa 5

print("--- ETAPA 1: Preparação dos Dados ---")
print(f"Quantidade de amostras: {X.shape[0]}")
print(f"Quantidade de atributos: {X.shape[1]}")
print("\nEstatísticas básicas:")
print(X.describe())
print("\n" + "="*50 + "\n")

# 2. Aplicação de Clusterização
print("--- ETAPA 2: Aplicação do K-Means ---")
for k in [2, 3, 4]:
    # Inicializando e treinando o K-Means
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    
    print(f"Resultados para k = {k}:")
    print("Centróides de cada cluster:")
    print(pd.DataFrame(kmeans.cluster_centers_, columns=iris.feature_names))
    
    counts = np.bincount(labels)
    for cluster_idx, count in enumerate(counts):
        print(f"-> Cluster {cluster_idx}: {count} elementos")
    print("-" * 30)

# 3. Visualização dos Clusters (Focando no k=3 para o gráfico)
# Treinando novamente para k=3 para gerar o gráfico
kmeans3 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels3 = kmeans3.fit_predict(X)

# Usaremos as duas últimas colunas (Petal Length e Petal Width) 
# pois elas geralmente oferecem a melhor visualização em 2D para este dataset.
plt.figure(figsize=(8, 6))
plt.scatter(X.iloc[:, 2], X.iloc[:, 3], c=labels3, cmap='viridis', edgecolors='k', s=50)
plt.scatter(kmeans3.cluster_centers_[:, 2], kmeans3.cluster_centers_[:, 3], 
            c='red', marker='X', s=200, label='Centróides')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title('Visualização dos Clusters K-Means (k=3)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 5. Comparação (Etapa Final para k=3)
print("\n" + "="*50 + "\n")
print("--- ETAPA 5: Comparação com as Classpy --versiones Reais (Para k=3) ---")

# Para calcular a matriz de confusão, precisamos "mapear" o número do cluster 
# criado pelo K-Means para o rótulo real mais frequente dentro daquele cluster.
labels_mapped = np.zeros_like(labels3)
for i in range(3):
    mask = (labels3 == i)
    # Encontra a classe real mais frequente neste cluster
    most_frequent_class = mode(y_true[mask], keepdims=True)[0][0]
    labels_mapped[mask] = most_frequent_class

cm = confusion_matrix(y_true, labels_mapped)
accuracy = np.mean(labels_mapped == y_true) * 100

print("Matriz de Confusão:")
print(cm)
print(f"\nPorcentagem de correspondência (Acurácia): {accuracy:.2f}%")