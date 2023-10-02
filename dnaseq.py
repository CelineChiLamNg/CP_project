# DNAnew(): retorna a a sequência vazia implementada como a lista vazia
def DNAnew():
    return []

# DNAadd(w,c): recebe uma sequência w e um inteiro c representando e DNA e retorna a sequência
# em que foi adicionada a letra c (c é um inteiro em {0,1,2,3})
def DNAadd(w, c):
    if c in range(0, 4):
        return w + [c]
    else:
        raise ValueError("c tem de ser 0,1,2 ou 3")
        
# DNAlen(w): recebe uma sequência w e retorna o comprimento da mesma
def DNAlen(w):
    return len(w)

# DNApos(w,i): recebe uma sequência w e um natural i e retorna a letra (inteiro)
# nessa posição onde a primeira posição é a posição indexada por ‘0’
def DNApos(w, i):
    return w[i]

# DNAoverlay(w,w’): recebe duas sequências w e e w’ e retorna o comprimento 
# do maior sufixo de w que é prefixo de w’
def DNAoverlay(W, w):
    max = 0
    if len(W) < len(w):
        length_of_shorter_fragment = len(W)
    else:
        length_of_shorter_fragment = len(w)

    for i in range(length_of_shorter_fragment):
        if DNAsuffix(W, i) == DNAprefix(w, i):
            max = i
    return max

# DNAoccursQ(w,w’): recebe duas sequências w e w’ e retorna True sse w ocorre em w’
def DNAoccursQ(W, w):
    W = list(map(lambda x: str(x), W))
    w = list(map(lambda x: str(x), w))
    return ''.join(W) in ''.join(w)

# DNAprefix(w,n): recebe uma sequência w e retorna o prefixo de tamanho n
# (caso n seja menor our igual ao comprimento de w)
def DNAprefix(w, n):
    if n <= len(w):
        return w[:n]
    raise ValueError("Não é possível definir um prefixo com tamanho superior ao comprimentoda sequência")
    
# DNAsuffix(w,n): recebe uma sequência w e retorna o sufixo de tamanho n
def DNAsuffix(w, n):
    if n == 0:
        return []
    if n <= len(w):
        return w[-n:]
    raise ValueError("Não é possível definir um sufixo com tamanho superior ao comprimento da sequência")
    
# DNAconc(w,w’): recebe duas sequências w e w’ e retorna a concatenação da sequência w com a sequência w’
def DNAconc(w, W):
    return w + W