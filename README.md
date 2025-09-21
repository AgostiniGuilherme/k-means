Clusterização K-Means – Iris Dataset

Este projeto implementa o algoritmo K-Means em Python, aplicado ao famoso dataset Iris, com duas versões:

Implementação do zero (hardcore/scratch)

Implementação usando sklearn

O objetivo é comparar qualidade e desempenho entre as duas abordagens.

🔎 O que é K-Means?

K-Means é um algoritmo de aprendizado não supervisionado usado para clustering (agrupamento) de dados. O objetivo é dividir um conjunto em k grupos (clusters), onde cada ponto pertence ao cluster cujo centróide está mais próximo.

Como funciona o algoritmo (versão do zero):

Inicialização: Escolhe k centróides aleatórios.

Atribuição: Cada ponto é associado ao centróide mais próximo (distância euclidiana).

Atualização: Os centróides são recalculados como a média dos pontos do cluster.

Repetição: Os passos 2–3 são repetidos até os centróides estabilizarem.

📂 Estrutura do Código
Implementações:

kmeans_iris_scratch.py → Algoritmo implementado manualmente (puro NumPy).

kmeans_iris_sklearn.py → Algoritmo usando sklearn.cluster.KMeans.

relatorio.txt → Comparação e análise dos resultados.

Funções principais (scratch):

inicializar_centroides() → Escolhe centróides iniciais.

atribuir_clusters() → Calcula distâncias e define clusters.

atualizar_centroides() → Recalcula centróides.

kmeans() → Controla a execução até a convergência.

Dataset utilizado:

Iris Dataset: 150 amostras de flores íris com 4 características:

Comprimento da sépala

Largura da sépala

Comprimento da pétala

Largura da pétala

(Obs: a variável target foi ignorada na clusterização.)

▶️ Como executar
Pré-requisitos:
pip install numpy scikit-learn

Execução:
# Versão implementada do zero
python kmeans_iris_scratch.py

# Versão sklearn
python kmeans_iris_sklearn.py

📊 Resultados gerados

Ambas as implementações executam os experimentos com k=3 e k=5 clusters e geram:

centroides_scratch_k*.npy / clusters_scratch_k*.npy

centroides_sklearn_k*.npy / clusters_sklearn_k*.npy

resultados_scratch.txt

resultados_sklearn.txt

Métricas avaliadas:

Silhouette Score (qualidade do clustering, -1 a 1, quanto maior melhor).

Tempo de execução (desempenho).

Resultados obtidos (exemplo real):
[Scratch] k=3 silhouette=0.5528 tempo=0.0088s
[Scratch] k=5 silhouette=0.4931 tempo=0.0024s

[Sklearn] k=3 silhouette=0.5528 tempo=3.3947s
[Sklearn] k=5 silhouette=0.4912 tempo=0.0481s

Interpretação:

O melhor valor foi k=3, que corresponde naturalmente às 3 espécies do Iris.

A versão scratch foi mais rápida (código simples), mas menos robusta.

A versão sklearn foi mais lenta (faz várias inicializações por padrão), porém mais estável.

📌 Conclusão

A implementação do zero reforçou o entendimento interno do K-Means.

O sklearn demonstrou melhor robustez e praticidade em aplicações reais.

O PCA (não mostrado aqui, mas disponível nos scripts) permitiu visualizar os clusters em 1D e 2D, confirmando que k=3 é a melhor escolha.