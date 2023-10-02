from dnaseq import DNAoccursQ

# Flnew(): retorna a lista de fragmentos vazia
def Flnew():
    return []

# Fladd(l,w): recebe uma lista de fragmentos l e uma sequência w e retorna a lista onde se adicionou w a l no fim da lista
def Fladd(l, w):
    return l + [w]

#FLpurge(l): retira a lista onde se retiraram as sequências irrelevantes.
def FLpurge(l):
    purged_list = l.copy()

    for i in range(len(purged_list)):  # vamos fixar no i e percorrer os j todos

        break_condition = False
        j = 0
        while j < len(purged_list) and not break_condition:

            # i != j porque não faz sentido comparar a sequência consigo mesma
            if i != j:
                first = purged_list[i]
                second = purged_list[j]

                if purged_list[i] is not None and purged_list[j] is not None:
                    is_sublist = DNAoccursQ(first, second)
                    if is_sublist:
                        purged_list[i] = None
                        break_condition = True
            j += 1
    purged_list = list(filter(lambda x: x is not None, purged_list))
    # filter: returns an iterator were the items are filtered through a function to test if the item is accepted or not
    return purged_list


# FLlen(l): recebe uma lista de fragmentos l e retorna o comprimento da mesma
def FLlen(l):
    return len(l)

# FLpos(l,i): recebe uma sequência w e um natural i e retorna a sequência nessa posição
def FLpos(l, i):
    return l[i]
