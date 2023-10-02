import dnapaths
import fraglist
import utils
import dnaseq
import graph

# retorna grafo com respetivos pesos, utilizando a meugrafo(empty) e purgedfrag
def grafo_pesos(purgedfrag):
    meugrafo = graph.GRnew(fraglist.FLlen(purgedfrag))
    # empty
    i = 0
    while i < fraglist.FLlen(purgedfrag):
        j = 0
        while j < fraglist.FLlen(purgedfrag):
            if i != j:
                peso = dnaseq.DNAoverlay(purgedfrag[i], purgedfrag[j])
                graph.GRadd(meugrafo, i, j, peso)  # colocar pesos em cada posicao
            j += 1
        i += 1
    return meugrafo


# 3a
def pesos_no_inicial(grafo):
    # deve receber grafo com pesos -> grafo
    pesomax = []  # lista de pesos que vai ser usado no sample
    for i in range(graph.GRnnodes(grafo)):
        pesomax.append(graph.GRindegree(grafo, i))
        # retorna o max dos pesos cujos vertices tem destino no i
    return pesomax

#n foi usado
def criar_novo_caminho(grafo, no_inicial):  # deve receber meugrafo -> grafo com pesos
    return dnapaths.Pnew(grafo, no_inicial)
    # novo caminho a partir de nó "no_inicial"


# 3b
#n foi usado
def HamilexQ(grafo, caminho):
    if (not (dnapaths.PHamiltonianQ(grafo, caminho))) and dnapaths.PextendableQ(grafo, caminho):
        return True
    else:
        return False

#nao foi usado
def continuar_caminho(grafo, caminho):
    proximo_no = utils.sample((graph.GRadj(grafo, caminho[-1])).pop(), 2)
    caminho = dnapaths.Padd(grafo, caminho, proximo_no)


# 3c
'''
Caso p seja um caminho Hamiltoniano verificar DNAlen(Pseq(g,p)) é a menor
até ao momento e nestas condições guardar p como o resultado r
'''

#n foi usado
def comparar_sequencias(grafo, purgedfrag, caminho):
    a = None
    length_a = 0
    y = 0
    if y == 0:  # voltinhas
        a = dnapaths.Pseq(grafo, caminho, purgedfrag)
        length_a = dnaseq.DNAlen(a)
    elif y > 0:  # voltinhas
        b = dnapaths.Pseq(grafo, caminho, purgedfrag)
        length_b = dnaseq.DNAlen(b)
        if length_b < length_a:
            a = b
            length_a = length_b
    y += 1
    return a


def encontrar_primeiro_no(grafo):
    primeiro_no = utils.sample(pesos_no_inicial(grafo), -2)
    return primeiro_no


def encontrar_proximo_no(grafo, caminho):
    posicao_pesos_dos_nos_adj = graph.GRadj(grafo, caminho[-1])
    posicao_dos_nos_adj = posicao_pesos_dos_nos_adj[0]
    pesos_dos_nos_adj_connections = posicao_pesos_dos_nos_adj[1]

    qual_peso = utils.sample(pesos_dos_nos_adj_connections, 2)

    return posicao_dos_nos_adj[qual_peso]

frag=utils.generate(100, 50, 20, 100)

def algoritmo(frag, k):
    purgedfrag = fraglist.FLpurge(frag)
    #print(purgedfrag)
    dna_mais_curto_ate_agr = None

    if fraglist.FLlen(purgedfrag) == 1:
        dna_mais_curto_ate_agr = purgedfrag[0]

    grafo = grafo_pesos(purgedfrag)

    for counter in range(k):

        # 3a
        no_inicial = encontrar_primeiro_no(grafo)

        p = dnapaths.Pnew(grafo, no_inicial)

        # 3b
        while not dnapaths.PHamiltonianQ(grafo, p) and dnapaths.PextendableQ(grafo, p):

            proximo_no = encontrar_proximo_no(grafo, p)
            dnapaths.Padd(grafo, p, proximo_no)

            if dnapaths.PHamiltonianQ(grafo, p):
                dna_encontrado = dnapaths.Pseq(grafo, p, purgedfrag)         

                if dna_mais_curto_ate_agr is not None:
                    if dnaseq.DNAlen(dna_encontrado) < dnaseq.DNAlen(dna_mais_curto_ate_agr):
                        dna_mais_curto_ate_agr = dna_encontrado
                else:
                    dna_mais_curto_ate_agr = dna_encontrado
    return dna_mais_curto_ate_agr