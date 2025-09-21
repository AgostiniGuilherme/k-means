RELATÓRIO – Clusterização com KMeans na Base Iris

1. Base de Dados
Utilizamos a base Iris, que contém 150 instâncias e 4 atributos (comprimento e largura das sépalas e pétalas). 
A variável de classe (target) foi desconsiderada durante os experimentos, como solicitado.

2. Implementações
Foram realizados dois tipos de implementação:
- KMeans do zero (“hardcore”): desenvolvido manualmente, apenas utilizando bibliotecas básicas como Numpy para cálculos.
- KMeans via biblioteca (sklearn): utilizando a classe sklearn.cluster.KMeans, já implementada.

3. Experimentos
Foram feitos experimentos com duas quantidades de clusters:
- k = 3
- k = 5

Em ambos os casos, os algoritmos foram executados e avaliados com a métrica Silhouette Score, que mede a qualidade da separação dos clusters (quanto mais próximo de 1, melhor).

4. Avaliação (Métricas e Desempenho)
- O algoritmo hardcore implementado do zero apresentou valores de silhouette próximos aos do sklearn, confirmando que a implementação está correta.
- O algoritmo sklearn foi ligeiramente mais rápido, pois é otimizado em C e possui técnicas de inicialização e convergência mais eficientes.
- Ambos tiveram desempenho adequado, mas a versão sklearn mostrou maior consistência nos resultados.

(Obs: Os valores exatos de tempo de execução e silhouette variam a cada execução, mas foram salvos em arquivos resultados_scratch.txt e resultados_sklearn.txt.)

5. PCA – Redução de Dimensionalidade
Após identificar o melhor valor de k (aquele com melhor silhouette, normalmente k=3), aplicamos a técnica PCA para reduzir a dimensionalidade:
- PCA com 1 componente: os dados foram projetados em um eixo único. Foi possível visualizar a separação parcial dos clusters, mas com sobreposição maior.
- PCA com 2 componentes: os dados foram projetados em um plano 2D. Os clusters ficaram mais bem separados, permitindo visualizar centróides e agrupamentos de forma clara.

6. Análise Comparativa
- Silhouette Score: Ambos os algoritmos obtiveram resultados próximos, confirmando que a implementação manual reproduz corretamente o funcionamento do KMeans.
- Tempo de execução: sklearn foi mais rápido devido à sua implementação otimizada.
- Visualização: Com PCA em 2 componentes, foi possível verificar que k=3 gera agrupamentos mais naturais na base Iris, o que confirma a qualidade da clusterização.

7. Conclusão
O trabalho permitiu compreender tanto a teoria quanto a prática do algoritmo KMeans:
- Implementação manual consolidou o entendimento do funcionamento interno (inicialização de centróides, atribuição de pontos e atualização iterativa).
- Implementação via sklearn mostrou como aplicar uma versão otimizada para aplicações reais.
- A comparação entre os métodos demonstrou que, embora a versão manual seja funcional, bibliotecas especializadas oferecem maior eficiência.
- O PCA evidenciou visualmente a qualidade dos agrupamentos, especialmente para k=3, considerado o valor mais adequado para o conjunto Iris.

Arquivos gerados:
- resultados_scratch.txt: resultados do algoritmo manual
- resultados_sklearn.txt: resultados do sklearn
- centroides_scratch_k{K}.npy / clusters_scratch_k{K}.npy
- centroides_sklearn_k{K}.npy / clusters_sklearn_k{K}.npy
