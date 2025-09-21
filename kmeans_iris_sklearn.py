"""
kmeans_iris_sklearn.py

Implementação usando sklearn.KMeans no conjunto Iris.
- Carrega Iris via sklearn
- Executa KMeans para k=3 e k=5
- Calcula silhouette_score
- Salva resultados em arquivos .txt e .npy

Como usar:
python kmeans_iris_sklearn.py
"""

import time
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def main():
    iris = load_iris()
    X = iris.data.copy()

    valores_k = [3, 5]
    resultados = {}

    for k in valores_k:
        inicio = time.time()
        modelo = KMeans(n_clusters=k, n_init=10, random_state=42)
        clusters = modelo.fit_predict(X)
        fim = time.time()

        tempo = fim - inicio
        sil = silhouette_score(X, clusters)

        resultados[k] = {'tempo': tempo, 'silhouette': sil}

        np.save(f'centroides_sklearn_k{k}.npy', modelo.cluster_centers_)
        np.save(f'clusters_sklearn_k{k}.npy', clusters)

        print(f"[Sklearn] k={k} silhouette={sil:.4f} tempo={tempo:.4f}s")

    with open('resultados_sklearn.txt', 'w') as f:
        for k, v in resultados.items():
            f.write(f"k={k} silhouette={v['silhouette']:.6f} tempo={v['tempo']:.6f}\n")


if __name__ == '__main__':
    main()
