🔹 Código Hardcore 
k=3 silhouette=0.552819 tempo=0.008801
k=5 silhouette=0.493080 tempo=0.002352


Como funciona:
Inicializa centróides aleatórios.
Atribui cada ponto ao centróide mais próximo (usando distância euclidiana).
Atualiza os centróides calculando a média dos pontos de cada cluster.
Repete até convergir.
Avalia os agrupamentos com o silhouette score.
Resultado obtido:
k=3 → silhouette = 0.5528, tempo = 0.0088s
k=5 → silhouette = 0.4931, tempo = 0.0024s
👉 Mostra que o algoritmo manual funcionou corretamente e muito rápido, já que o código é simples e roda só em Python/Numpy.


🔹 Código com Sklearn

k=3 silhouette=0.552819 tempo=3.394740
k=5 silhouette=0.491240 tempo=0.048113


Como funciona:
Usa a classe KMeans do sklearn, que já implementa de forma otimizada em C/Fortran.
Executa com os mesmos dados e valores de k.
Calcula o silhouette score e mede tempo de execução.
Resultado obtido:
k=3 → silhouette = 0.5528, tempo = 3.3947s
k=5 → silhouette = 0.4912, tempo = 0.0481s
👉 O resultado é praticamente o mesmo em termos de qualidade do cluster, mas o tempo foi maior porque o sklearn roda inicializações múltiplas (n_init=10 por padrão), garantindo robustez.


🔹 Conclusão dos Resultados
Ambos os códigos chegaram nos mesmos valores de silhouette, confirmando que a implementação hardcore está correta.
Para k=3, o agrupamento foi melhor (silhouette maior). Isso faz sentido, já que o Iris naturalmente tem 3 classes.
O sklearn foi mais lento nessa execução, mas mais robusto (faz várias inicializações para evitar cair em mínimos locais).
O scratch foi mais rápido, mas não garante estabilidade em todas as execuções.