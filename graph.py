# recebe um natural n e retorna o grafo sem arestas com n nós (ou seja a matriz nxn com todas as entradas a 0). 
# A ideia é que os nós serão naturais (a começar em 0) que são índices dos fragmentos nas lista de fragmentos
def GRnew(n):
    return [[0 for i in range(n)] for j in range(n)]


# recebe um grafo g e dois nós (que são dois naturais) i e j e um peso natural w e adiciona a aresta de i para j com peso w
# (ou seja, coloca w na entrada i,j da matriz de adjacência de g)
def GRadd(g, i, j, w):
    if i == j:
        raise ValueError("You shouldn't modify how many times one node is connected to itself, it's always zero")
    g[i][j] = w


# recebe um grafo g e dois nós (que são dois naturais) i e j e retorna True sse há uma aresta (com peso superior a 0) do nó i ra o nó j
def GRadjQ(g, i, j):
    return g[i][j] > 0


# recebe um grafo g e um nó i e retorna uma lista com dois elementos:
# o primeiro elemento é a lista de nós adjacentes a i;
# o segundo é a lista de pesos das arestas de i para esses nós;
def GRadj(g, i):  # i vai nos definir a linha
    p = []  # primeira lista
    s = []  # segunda lista
    r = 0  # r vai nos definir a coluna
    while r < len(g):  # r nao pode ultrapassar a quantidade de colunas q temos
        if g[i][r] != 0:  # só adicionamos às listas se forem adjecentes (maior q 0 ou até podemos escrever !=0, mesma coisa)
            p += [r]  # adicionar r à lista p
            s += [g[i][r]]  # adicionar o peso(valor que está na posicao [i][r]) à lista s
        r += 1  # fazer r variar de inicio até ao fim
    return [p, s]


# recebe um grafo g e um nó i e retorna o máximo dos pesos das arestas cujo o destino é i
def GRindegree(g, i):
    r = 0
    m = 0
    while r < len(g):  # r tem de estar dentro de linhas do grafo
        if g[r][i] > m:  # comparar o valor antigo com o da proxima linha, se for maior entao guarda
            m = g[r][i]
        r += 1
    return m if m != 0 else 0.0001


# recebe um grafo g e retorna o número de nós de g.
def GRnnodes(g):
    return len(g)
