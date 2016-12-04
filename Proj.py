#86416 Francisco Sousa

#TIPOS ABSTRATOS DE DADOS
#Tipo Posicao:
# Construtor
def faz_pos(l, c):
    if not (isinstance(l, int) and isinstance(c, int) and l>=0 and c>=0):
        raise ValueError("Argumentos Invalidos")
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
#L = ("A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
#l = tuple(L)
#mgc = "A MARIA E GENIAL A PROGRAMAR EM PYTHON"

def mgc_so_letras(mgc):
    '''Recebe uma cadeia de caracteres e devolve pela mesma ordem os caracteres
    dela que estao contidos no tuplo L.'''
    mgc_letras=""
    for car in mgc:
        if car in L:
            mgc_letras = mgc_letras + car
    return mgc_letras

def gera_chave(l, mgc):
    '''Recebe dois argumentos, um tuplo de 25 letras e uma cadeia de caracteres,
    constituida por letras desse tuplo. Devolve uma chave, na forma de tuplo, em
    que a primeira parte sao as letras da cadeia de caracteres, sem espacos nem
    repeticoes e o resto sao as letras do tuplo que nao aparecem na cadeia.'''
    mgc_sl = mgc_so_letras(mgc)
    if not (isinstance(l, tuple) and len(l) == 25 and isinstance(mgc, str)):
        raise ValueError("Tipo de argumentos invalido!")
    elif len([ letra for letra in l if not isinstance(letra, str) ]) != 0:
        #Percorre o tuplo l e, para cada letra, verifica se eh uma string.
        #As letras que nao forem strings vao ser adicionadas a uma lista. Se o
        #comprimento desta lista for diferente de zero, levanta o erro.
        raise ValueError("Todos os membros do primeiro argumento devem ser strings!")
    elif len([ letra for letra in l if letra not in L ]) != 0:
        #Percorre o tuplo l e, para cada letra, verifica se pertence a L.
        #As letras que nao pertencerem vao ser adicionadas a uma lista. Se o
        #comprimento desta lista for diferente de zero, levanta o erro.        
        raise ValueError("Todos os elementos do primeiro argumento devem ser letras maiusculas!")
    elif len([ l[i] for i in range(len(l)) if l[i] in l[0:i] ]) != 0:   
        #Percorre o range do comprimento do tuplo l e, para cada indice i,
        #verifica se a letra com esse indice l[i] ja apareceu antes em l. As
        #letras que aparecerem mais do que uma vez vao ser adicionadas a uma
        #lista. Se o comprimento dela for diferente de zero, levanta o erro.        
        raise ValueError("Nao devem haver elementos repetidos no primeiro argumento!")
    elif len([ car for car in mgc_sl if car not in l ]) != 0:
        #Percorre a cadeia mgc sem espaços mgc_sl e, para cada caracter,
        #verifica se esta contido no tuplo l. Devolve uma lista com os caracteres
        #que nao satisfazem esta condicao. Se esta lista tiver algum elemento,
        #retorna o erro.
        raise ValueError("Os caracteres do segundo argumento devem pertencer ao primeiro!")
    else:
        compacto = ()
        resto = ()
        for car in range( len(mgc_sl) ): #Remove os elementos repetidos do mgc_sl
            if mgc_sl[car] not in compacto:
                compacto = compacto + (mgc_sl[car],)
        for letra in range(len(l)): #Filtra os elementos de l ja em mgc_sl
            if l[letra] not in compacto:
                resto = resto + (l[letra],)
        return compacto + resto

def gera_chave_linhas(l, mgc):

    '''Recebe dois argumentos, um tuplo de 25 letras e uma cadeia de caracteres, constituida por letras desse tuplo. Devolve uma chave,'''
    if isinstance(l, tuple) and len(l)==25 and isinstance(mgc, str):
        raise ValueError("Tipo de Argumentos Invalido")
    elif len([letra for letra in l if (not isinstance(letra, str))]):
        '''Coisas'''
        raise ValueError("Argumentos Invalidos")
    elif len([car for car in l if (not isinstance(car,str))]):
        raise ValueError("Argumentos Invalidos")
    else:
        compact=()
        resto=()
        for car in range(len(mgc)):
                if mgc[car] not in compact:
                    compact = compact + (mgc[car],)
        for letra in range(len(l)):
                if l[letra] not in compact:
                    resto = resto + (l[letra],)
        return compact + resto        

# Seletor
def ref_chave(c, p):
    '''Ola'''

    '''Recebe dois argumentos, um tuplo de 25 letras e uma cadeia de caracteres,
    constituida por letras desse tuplo. Devolve uma chave, na forma de tuplo, em
    que a primeira parte sao as letras da cadeia de caracteres, sem espacos nem
    repeticoes e o resto sao as letras do tuplo que nao aparecem na cadeia,
    estando todas estas letras dispostas em tuplos de 5 elementos.'''    
    chave = gera_chave(l, mgc)
    chave_linhas = ()
    for lin in range(5):
        linha = ()
        for col in range(5):
            linha = linha + (chave[5*lin + col],)
        chave_linhas = chave_linhas + (linha,)
    return chave_linhas
    
# Seletor
def ref_chave(c, p):
    '''Recebe uma chave e uma posicao e devolve a letra dessa chave na posicao.'''
    lin = p[0]
    col = p[1]
    return c[lin][col]

# Modificador
def muda_chave(c, p, l):
    nova_chave = c
    lin = p[0]
    col = p[1]    
    nova_chave[lin][col] = l
    return nova_chave

