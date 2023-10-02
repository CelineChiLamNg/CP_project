import dnaseq
import graph

# Pnew(g,i): recebe um grafo g e um nó i e retorna o caminho vazio que começa no nó i do grafo g
def Pnew(g, i):
    if i > len(g) or i < 0:
        raise ValueError('i precisa de estar no grafo com dimensão n, logo precisa de ser um inteiro entre 0 e len(g)')
    return [i]

# Padd(g,p,j): recebe um grafo g, um caminho p e um nó j adiciona o nó ao fim do caminho
# se j for adjacente ao último elemento de p entao adiciona
def Padd(g, p, j):
    if j >= graph.GRnnodes(g):
        raise ValueError('j=' + str(j) + " não está no grafo")
    if g[p[-1]][j] != 0:
        p.append(j)
    else:
        raise ValueError("O nó não é adjacente ao último elemento do caminho")
        
# PloopQ(g,p): recebe um grafo g e um caminho p e retorna True sse o último nó do caminho está num ciclo do caminho
def Ploop(g, p):
    for i in range(0, len(p) - 2):
        if p[-1] == p[i]:
            return True
    return False

# PHamiltonianQ(g,p): recebe um grafo g e um caminho p e retorna True sse p é Hamiltoniano no grafo g
def PHamiltonianQ(g, p):
    def VerticesTodosQ(g, p):
        return len(g) == len(p)

    def RepititionQ(g, p):
        r = False
        i = 0
        while i < (len(p)) and not r:
            for j in range(len(p)):
                if i != j:
                    if p[j] == p[i]:
                        r = True
            i += 1
        return r

    return VerticesTodosQ(g, p) and not RepititionQ(g, p)

# PextendableQ(g,p): recebe um grafo g e um caminho p e retorna True sse p pode ser estendido sem criar ciclos
# adiciona +1 nó que nao esteja já a ser utilizado no caminho
def PextendableQ(g, p):
    p_copia = p.copy()
    r = False
    v = 0
    while v < graph.GRnnodes(g) and not r:

        if graph.GRadjQ(g, p_copia[-1], v):
            Padd(g, p_copia, v)
            if not Ploop(g, p_copia):
                r = True
        v = v + 1
    return r

# Pseq(g,p,l): recebe um grafo g, um caminho p e a lista de sequências l e retorna a sequência de DNA gerada pelo caminho
# (usando apenas as funções da interface de sequência de DNA)
def Pseq(g, p, purgedfragments):
    def DNAconcat2(w1, w2):
        return dnaseq.DNAconc(w1, dnaseq.DNAsuffix(w2, len(w2) - dnaseq.DNAoverlay(w1, w2)))

    r = dnaseq.DNAnew()
    for v in p:
        r = DNAconcat2(r, purgedfragments[v])
    return r