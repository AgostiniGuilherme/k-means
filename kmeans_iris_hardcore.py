"""
kmeans_iris_hardcore.py

Implementação manual do algoritmo K-Means para o conjunto de dados Iris.
- Carrega Iris via sklearn
- Executa KMeans implementado do zero
- Testa com k=3 e k=5
- Calcula silhouette_score
- Salva resultados em arquivos .txt e .npy

Como usar:
python kmeans_iris_hardcore.py
"""

import time
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score


def inicializar_centroides(dados, k, seed=42):
    np.random.seed(seed)
    indices = np.random.choice(len(dados), k, replace=False)
    return dados[indices]


def atribuir_clusters(dados, centroides):
    distancias = np.linalg.norm(dados[:, np.newaxis] - centroides, axis=2)
    return np.argmin(distancias, axis=1)


def atualizar_centroides(dados, clusters, k):
    novos_centroides = []
    for i in range(k):
        pontos = dados[clusters == i]
        if len(pontos) > 0:
            novos_centroides.append(pontos.mean(axis=0))
        else:
            novos_centroides.append(dados[np.random.randint(0, len(dados))])
    return np.array(novos_centroides)


def kmeans(dados, k, max_iter=300, tol=1e-4):
    centroides = inicializar_centroides(dados, k)
    for _ in range(max_iter):
        clusters = atribuir_clusters(dados, centroides)
        novos_centroides = atualizar_centroides(dados, clusters, k)
        if np.allclose(centroides, novos_centroides, atol=tol):
            break
        centroides = novos_centroides
    return clusters, centroides


def main():
    iris = load_iris()
    X = iris.data.copy()

    valores_k = [3, 5]
    resultados = {}

    for k in valores_k:
        inicio = time.time()
        clusters, centroides = kmeans(X, k)
        fim = time.time()

        tempo = fim - inicio
        sil = silhouette_score(X, clusters)

        resultados[k] = {'tempo': tempo, 'silhouette': sil}

        np.save(f'centroides_hardcore_k{k}.npy', centroides)
        np.save(f'clusters_hardcore_k{k}.npy', clusters)

        print(f"[Hardcore] k={k} silhouette={sil:.4f} tempo={tempo:.4f}s")

    with open('resultados_hardcore.txt', 'w') as f:
        for k, v in resultados.items():
            f.write(f"k={k} silhouette={v['silhouette']:.6f} tempo={v['tempo']:.6f}\n")


if __name__ == '__main__':
    main()
# ---------------------- Implementação do K-Means do zero ----------------------