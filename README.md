# Clusterização K-Means – Iris Dataset

Este projeto implementa o algoritmo K-Means **do zero** em Python, aplicado ao dataset clássico **Iris**, e também apresenta uma versão comparativa utilizando a biblioteca **scikit-learn**.

## O que é K-Means?

K-Means é um algoritmo de aprendizado **não supervisionado** usado para **clustering** (agrupamento) de dados. O objetivo é dividir um conjunto de dados em `k` grupos (clusters), onde cada ponto pertence ao cluster cujo centroide está mais próximo.

### Funcionamento do algoritmo:

1. **Inicialização**: Escolhe `k` centroides aleatoriamente  
2. **Atribuição**: Cada ponto é associado ao centroide mais próximo  
3. **Atualização**: Os centroides são recalculados como a média dos pontos atribuídos  
4. **Repetição**: O processo continua até os centroides estabilizarem  

---

## Estrutura do Repositório

- `kmeans_iris_hardcore.py` → Implementação **do zero** usando apenas NumPy 
- `kmeans_iris_sklearn.py` → Implementação utilizando `scikit-learn` para comparação  

- Arquivos de saída gerados:  
  - `centroides_<versao>_k3.npy` / `centroides_<versao>_k5.npy`  
  - `clusters_<versao>_k3.npy` / `clusters_<versao>_k5.npy`  
  - `resultados_<versao>.txt` (resumo com métricas)  
  
---

## Dataset Utilizado

**Iris Dataset**: 150 amostras de flores íris com 4 atributos:  
- Comprimento da sépala  
- Largura da sépala  
- Comprimento da pétala  
- Largura da pétala  

---

## Como Executar

### Pré-requisitos:
```bash
pip install numpy scikit-learn
```

### Rodar versão implementada do zero:
```bash
python kmeans_iris_hardcore.py
```

### Rodar versão com scikit-learn:
```bash
python kmeans_iris_sklearn.py
```

---

## Resultados Obtidos

O algoritmo foi testado para `k=3` (ideal para o dataset Iris) e `k=5`.

### Métricas avaliadas:
- **Silhouette Score** → Qualidade do agrupamento (quanto maior, melhor)  
- **Tempo de execução** → Comparação entre implementação manual e sklearn  

### Exemplo de saída:

```
[Hardcore] k=3 silhouette=0.5528 tempo=0.0088s
[Hardcore] k=5 silhouette=0.4931 tempo=0.0024s

[Sklearn] k=3 silhouette=0.5528 tempo=3.3947s
[Sklearn] k=5 silhouette=0.4912 tempo=0.0481s
```

### Interpretação:
- Para **k=3**, o resultado é melhor (silhouette ~0.55), confirmando as 3 espécies do dataset.  
- Para **k=5**, a divisão excessiva reduz a qualidade (~0.49).  
- A versão **manual** roda mais rápido que a do `sklearn`, pois é otimizada para esse caso específico.  

---

## Características da Implementação

- ✅ Puro NumPy (versão hardcore)  
- ✅ Reprodutibilidade com seed fixa  
- ✅ Tratamento de clusters vazios  
- ✅ Avaliação com Silhouette Score  
- ✅ Comparação direta com `scikit-learn`  

