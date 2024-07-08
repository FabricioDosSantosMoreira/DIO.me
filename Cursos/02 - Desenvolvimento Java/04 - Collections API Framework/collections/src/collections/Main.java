// /Uma coleção (collection) é uma estrutura de dados que serve para agrupar muitos elementos 
// em uma única unidade; estes elementos precisam ser objetos.

// Uma Collection pode ter coleções homogêneas e heterogêneas, normalmente 
// utilizamos coleções homogêneas de um tipo específico.

// O núcleo principal das coleções é formado pelas interfaces da figura abaixo; essas 
// interfaces permitem manipular a coleção independentemente do nível de detalhe que elas representam.


// Temos quatro grandes tipos de coleções: List (lista), Set (conjunto), Queue (fila) e Map (mapa). 
// A partir dessas interfaces, temos muitas subclasses concretas que implementam várias formas diferentes de se trabalhar com cada coleção.

// / A classe Collections é uma classe utilitária do Java para operações comuns em coleções.


// Ela fornece métodos para ordenação, busca, manipulação e sincronização de coleções.
// O método sort() é usado para ordenar uma lista em ordem ascendente.
// O método sort() em conjunto com Collections.reverseOrder() permite ordenar em ordem descendente.


// Em Java, uma coleção (collection) refere-se a um objeto que agrupa múltiplos elementos em uma única unidade. As coleções são utilizadas para armazenar, manipular e transmitir dados de maneira eficiente. Existem várias interfaces e classes de coleções no Java, cada uma com finalidades específicas. Aqui estão alguns exemplos comuns de coleções em Java:

// Listas (Lists):

// ArrayList: Implementa uma lista redimensionável de arrays.
// LinkedList: Implementa uma lista duplamente ligada.
// Exemplo:

// java
// Copiar código
// List<String> nomes = new ArrayList<>();
// nomes.add("Alice");
// nomes.add("Bob");
// nomes.add("Carol");
// Conjuntos (Sets):

// HashSet: Implementa um conjunto não ordenado.
// TreeSet: Implementa um conjunto ordenado.
// Exemplo:

// java
// Copiar código
// Set<Integer> numeros = new HashSet<>();
// numeros.add(1);
// numeros.add(2);
// numeros.add(3);
// Mapas (Maps):

// HashMap: Implementa um mapeamento não ordenado de chaves e valores.
// TreeMap: Implementa um mapeamento ordenado de chaves e valores.
// Exemplo:

// java
// Copiar código
// Map<String, Integer> idadePorNome = new HashMap<>();
// idadePorNome.put("Alice", 30);
// idadePorNome.put("Bob", 25);
// idadePorNome.put("Carol", 35);
// Pilhas (Stacks):

// Stack: Implementa uma pilha LIFO (Last In, First Out).
// Exemplo:

// java
// Copiar código
// Stack<String> pilha = new Stack<>();
// pilha.push("A");
// pilha.push("B");
// pilha.push("C");
// Filas (Queues):

// LinkedList: Pode ser usada como uma fila FIFO (First In, First Out).
// PriorityQueue: Implementa uma fila com prioridade.
// Exemplo:

// java
// Copiar código
// Queue<String> fila = new LinkedList<>();
// fila.add("A");
// fila.add("B");
// fila.add("C");
