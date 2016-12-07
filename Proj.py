#86416 Francisco Sousa

#TIPOS ABSTRATOS DE DADOS
#Tipo Posicao:
# Construtor
def faz_pos(l, c):
    if not (isinstance(l, int) and isinstance(c, int) and l>=0 and c>=0):
        raise ValueError("faz_pos: argumentos errados")
    else:
        return (l, c)

# Selectores
def linha_pos(p):
    return p[0]

def coluna_pos(p):
    return p[1]

# Reconhecedores
def e_pos(arg):
    if not(isinstance(arg, tuple) and len(arg)==2 and isinstance(linha_pos(arg), int) and isinstance(coluna_pos(arg), int) and linha_pos(arg)>=0 and coluna_pos(arg)>=0):
        return False
    else:
        return True

# Testes
def pos_iguais(p1, p2):
    if linha_pos(p1)==linha_pos(p2) and coluna_pos(p1)==coluna_pos(p2):
        return True
    else:
        return False
    
#Tipo Chave:
# Construtores
L = ("A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
#l = tuple(L)
#mgc = "A MARIA E GENIAL A PROGRAMAR EM PYTHON"

def str_so_letras(strg):
    '''Recebe uma cadeia de caracteres e devolve pela mesma ordem os caracteres
    dela mas sem os espacos'''
    str_letras=""
    for car in strg:
        if car != " ":
            str_letras = str_letras + car
    return str_letras

def gera_chave(l, mgc):
    '''Recebe dois argumentos, um tuplo de 25 letras e uma cadeia de caracteres,
    constituida por letras desse tuplo. Devolve uma chave, na forma de lista, em
    que a primeira parte sao as letras da cadeia de caracteres, sem espacos nem
    repeticoes e o resto sao as letras do tuplo que nao aparecem na cadeia.'''
    if not (isinstance(l, tuple) and len(l) == 25 and isinstance(mgc, str)):
        return False
    elif len([ letra for letra in l if not isinstance(letra, str) ]) != 0:
        #Percorre o tuplo l e, para cada letra, verifica se eh uma string.
        #As letras que nao forem strings vao ser adicionadas a uma lista. Se o
        #comprimento desta lista for diferente de zero, levanta o erro.
        return False
    elif len([ letra for letra in l if letra not in L ]) != 0:
        #Percorre o tuplo l e, para cada letra, verifica se pertence a L.
        #As letras que nao pertencerem vao ser adicionadas a uma lista. Se o
        #comprimento desta lista for diferente de zero, levanta o erro.        
        return False
    elif len([ l[i] for i in range(len(l)) if l[i] in l[0:i] ]) != 0:   
        #Percorre o range do comprimento do tuplo l e, para cada indice i,
        #verifica se a letra com esse indice l[i] ja apareceu antes em l. As
        #letras que aparecerem mais do que uma vez vao ser adicionadas a uma
        #lista. Se o comprimento dela for diferente de zero, levanta o erro.        
        return False
    elif len([ car for car in str_so_letras(mgc) if car not in l ]) != 0:
        #Percorre a cadeia mgc sem espacos e, para cada caracter, verifica
        #se esta contido no tuplo l. Devolve uma lista com os caracteres
        #que nao satisfazem esta condicao. Se esta lista tiver algum elemento,
        #retorna o erro.
        return False
    else:
        mgc_sl = str_so_letras(mgc)        
        compacto = []
        resto = []
        for car in range( len(mgc_sl) ): #Remove os elementos repetidos do mgc_sl
            if mgc_sl[car] not in compacto:
                compacto = compacto + [mgc_sl[car]]
        for letra in range(len(l)): #Filtra os elementos de l ja em mgc_sl
            if l[letra] not in compacto:
                resto = resto + [l[letra]]
        return compacto + resto

def gera_chave_linhas(l, mgc):
    '''Recebe dois argumentos, um tuplo de 25 letras e uma cadeia de caracteres,
    constituida por letras desse tuplo. Devolve uma chave, na forma de lista, em
    que a primeira parte sao as letras da cadeia de caracteres, sem espacos nem
    repeticoes e o resto sao as letras do tuplo que nao aparecem na cadeia,
    estando todas estas letras dispostas em listas de 5 elementos.'''    
    chave = gera_chave(l, mgc)
    if chave == False:
        raise ValueError("gera_chave_linhas: argumentos errados")
    else:
        chave_linhas = []
        for lin in range(5):
            linha = []
            for col in range(5):
                linha = linha + [chave[5*lin + col]]
            chave_linhas = chave_linhas + [linha]
        return chave_linhas
    
# Seletor
def ref_chave(c, p):
    '''Recebe uma chave e uma posicao e devolve a letra dessa chave na posicao.'''
    return c[ linha_pos(p) ][ coluna_pos(p) ]

# Modificador
def muda_chave(c, p, l):    
    c[ linha_pos(p) ][ coluna_pos(p) ] = l
    return c

# Reconhecedores
def e_chave(arg):
    if isinstance(arg, list) and len(arg)==5 and len([ linha for linha in arg if len(linha) == 5 ]) == 5:
        lista = []
        for linha in arg:
            lista = lista + linha
        if len([ lista[l] for l in range(25) if lista[l] in lista[0:l] ]) == 0 and len([ letra for letra in lista if letra not in L ]) == 0:
            return True
    return False

# Transformadores
def string_chave(c):
    string = ""
    for lin in range(5):
        linha = ""
        for col in range(5):
            linha = linha + c[lin][col] + " "
        string = string + linha + "\n"
    return string


#FUNCOES A DESENVOLVER
#digramas
def digramas(mens):
    mens_sl = str_so_letras(mens)
    def digramas_rec(mens):
        if mens == "":
            return ""
        elif len(mens) == 1:
            return mens + "X"
        else:
            par = mens[0:2]
            if par[0] + par[0] == par:
                return par[0] + "X" + digramas(mens[1:])
            else:
                return par + digramas(mens[2:])
    return digramas_rec(mens_sl)

def procura_pos(l, chave):
    for lin in range( len(chave) ):
        for col in range( len(chave[lin]) ):
            if ref_chave(chave, faz_pos(lin, col)) == l:
                return faz_pos(lin, col)
#figura
def figura(digrm, chave):
    letra1, letra2 = digrm[0], digrm[1]
    pos1, pos2 = procura_pos(letra1, chave), procura_pos(letra2, chave)
    if linha_pos(pos1) == linha_pos(pos2):
        fig = 'l'
    elif coluna_pos(pos1) == coluna_pos(pos2):
        fig = 'c'
    else:
        fig = 'r'
    return (fig, pos1, pos2)
    
def codifica_uni(indice, inc):
    variacao = indice + inc
    return variacao % 5
    
#codifica_l    
def codifica_l(pos1, pos2, inc):
    pos1_cod = faz_pos( linha_pos(pos1), codifica_uni(coluna_pos(pos1), inc) )
    pos2_cod = faz_pos( linha_pos(pos2), codifica_uni(coluna_pos(pos2), inc) )
    return (pos1_cod, pos2_cod)

#codifica_c
def codifica_c(pos1, pos2, inc):
    pos1_cod = faz_pos( codifica_uni(linha_pos(pos1), inc), coluna_pos(pos1) )
    pos2_cod = faz_pos( codifica_uni(linha_pos(pos2), inc), coluna_pos(pos2) )
    return (pos1_cod, pos2_cod)

#codifica_r
def codifica_r(pos1, pos2):
    pos1_cod = faz_pos( linha_pos(pos1), coluna_pos(pos2) )
    pos2_cod = faz_pos( linha_pos(pos2), coluna_pos(pos1) )
    return (pos1_cod, pos2_cod)

#codifica_digrama
def codifica_digrama(digrm, chave, inc):
    fig = figura(digrm, chave)
    pos1 = fig[1]
    pos2 = fig[2]
    if fig[0] == 'l':
        pos_cod = codifica_l(pos1, pos2, inc)
    elif fig[0] == 'c':
        pos_cod = codifica_c(pos1, pos2, inc)
    elif fig[0] == 'r':
        pos_cod = codifica_r(pos1, pos2)
    return ref_chave(chave, pos_cod[0]) + ref_chave(chave, pos_cod[1])

#codifica
def codifica(mens, chave, inc):
    mens_cod = ""
    digrms = digramas(mens)
    for par in range(0, len(digrms), 2):
        dig = digrms[par] + digrms[par+1]
        mens_cod = mens_cod + codifica_digrama(dig, chave, inc)
    return mens_cod