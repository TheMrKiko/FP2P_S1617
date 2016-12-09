#86416 Francisco Sousa

#TIPOS ABSTRATOS DE DADOS
#Tipo Posicao:
# Construtor
def faz_pos(l, c):
    '''Recebe uma linha e uma coluna e retorna um tipo posicao com esses dados'''
    if not (isinstance(l, int) and isinstance(c, int) and l >= 0 and c >= 0):
        raise ValueError("faz_pos: argumentos errados")
    else:
        return (l, c)

# Selectores
def linha_pos(p):
    '''Devolve a linha de p'''
    return p[0]

def coluna_pos(p):
    '''Devolve a coluna de p'''
    return p[1]

# Modificador
def muda_pos(pos, coord, res):
    if coord == 0:
        return ( linha_pos(pos) + res, coluna_pos(pos) )
    else:
        return ( linha_pos(pos), coluna_pos(pos) + res )

# Reconhecedores
def e_pos(arg):
    '''Analisa o arg e devolve True se satisfazer as condicoes necessarias para ser
    uma posicao. Se nao, devolve False.'''
    if not(isinstance(arg, tuple) and len(arg)==2 and isinstance(linha_pos(arg), int) and isinstance(coluna_pos(arg), int) and linha_pos(arg) >= 0 and coluna_pos(arg) >= 0):
        return False
    else:
        return True

# Testes
def pos_iguais(p1, p2):
    '''Analisa de p1 e p2 sao a mesma posicao'''
    if linha_pos(p1) == linha_pos(p2) and coluna_pos(p1) == coluna_pos(p2):
        return True
    else:
        return False

#Tipo Chave:
# Construtores
L = ("A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

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

def mete_em_linhas(chave):
    '''Recebe uma chave com todos os caracteres numa unica lista e agrupa-os em
    5 listas de 5 caracteres'''
    chave_em_linhas = []
    for lin in range(5):
        linha = []
        for col in range(5):
            linha = linha + [chave[5*lin + col]]
        chave_em_linhas = chave_em_linhas + [linha]
    return chave_em_linhas

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
        return mete_em_linhas(chave)

def troca(coord):
    '''Recebe uma coordenada 0 ou 1 e devolve 1 ou 0 respetivamente'''
    return (coord + 1) % 2

def pos_valida(nova_pos, coord, posicoes):
    '''Recebe uma posicao, uma coordenada dessa posicao e um conjunto de posicoes
    e testa se essa posicao passa dos limites da chave 5x5 ou se ja esta contida
    no conjunto de posicoes'''
    if nova_pos[coord] == 5 or nova_pos[coord] == -1 or nova_pos in posicoes:
        return False
    else:
        return True

def cria_espiral(pos, coord, op, chave):
    '''Recebe uma posicao inicial, uma coordenada para alterar, uma operacao
    (+1 ou -1) e uma chave e, para o tamanho dessa chave e para essa posicao
    inicia, cria uma lista de posicoes que fazem uma espiral ao longo dessa
    chave, a comecar na posicao inicial'''
    posicoes = [pos] #espiral comeca com a posicao inicial
    for letra in range( len(chave) - 1 ): #para as restantes letras
        nova_pos = muda_pos(pos, coord, op) #calcula uma nova posicao,
            #somando ou subtraindo 1 a coordenada
        if not pos_valida(nova_pos, coord, posicoes):#testa se a posicao e valida
            coord = troca(coord) #se nao, troca de coordenada e repete a operacao
            nova_pos = muda_pos(pos, coord, op)#mas na outra coordenada
            if not pos_valida(nova_pos, coord, posicoes):#testa se ja e valida
                op = -op #se ainda nao for, muda a operacao e fa-la de novo
                nova_pos = muda_pos(pos, coord, op)
        pos = nova_pos #a posicao atual passa a ser a nova
        posicoes = posicoes + [pos] #adiciona a lista
    return posicoes

def cria_lista_vazia(el, leng):
    '''Recebe um comprimento e um elemento e enche uma lista desse comprimento
    com esses elementos'''
    lista = []
    for indice in range(leng):
        lista = lista + [el]
    return lista

def gera_chave_espiral(l, mgc, s, pos):
    '''Recebe um tuplo de 25 letras, uma cadeia de caracteres, um sentido (r ou c)
    e uma posicao. Devolve uma chave, em lista, mas a formar uma espiral de posicoes'''
    chave = gera_chave(l, mgc) #gera uma chave a partir de l e da mensagem
    if chave == False or s not in ('r','c') or not e_pos(pos):
        raise ValueError("gera_chave_espiral: argumentos errados")
    else:
        chave_espiral = []
        if s == 'r': #atribui valores iniciais a op e a coord consoante o s e o pos
            if pos[0] == 0:
                op = 1
            else:
                op = -1
            if pos[0]==pos[1]:
                coord = 1
            else:
                coord = 0
        elif s == 'c':
            if pos[1] == 0:
                op = 1
            else:
                op = -1
            if pos[0]==pos[1]:
                coord = 0
            else:
                coord = 1

        espiral = cria_espiral(pos, coord, op, chave) #usa os valores para criar a espiral
        chave_espiral = mete_em_linhas(cria_lista_vazia("", 25))#cria 5 listas de 5 vazias

        for indice in range( len(chave) ): #consoante as posicoes na espira, coloca
            lin = linha_pos( espiral[indice] )#cada letra da chave no posicao na
            col = coluna_pos( espiral[indice] )#chave espiral
            chave_espiral[lin][col] = chave[indice]

        return chave_espiral

# Seletor
def ref_chave(c, p):
    '''Recebe uma chave e uma posicao e devolve a letra dessa chave na posicao.'''
    return c[ linha_pos(p) ][ coluna_pos(p) ]

# Modificador
def muda_chave(c, p, l):
    '''Recebe uma chave, uma posicao e uma letra e altera a chave, colocando a
    letra na posicao'''
    c[ linha_pos(p) ][ coluna_pos(p) ] = l
    return c

# Reconhecedores
def e_chave(arg):
    '''Analisa o arg e devolve True se satisfazer as condicoes necessarias para ser
    uma chave. Se nao, devolve False.'''
    if isinstance(arg, list) and len(arg) == 5 and len([ linha for linha in arg if len(linha) == 5 ]) == 5:
        lista = []
        for linha in arg:
            lista = lista + linha
        if len([ lista[l] for l in range(25) if lista[l] in lista[0:l] ]) == 0 and len([ letra for letra in lista if letra not in L ]) == 0:
            return True
    return False

# Transformadores
def string_chave(c):
    '''Transforma a chave numa cadeia de caracteres, que ao ser impressa, forma
    uma tabela 5x5'''
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
    '''Recebe uma cadeia de caracteres. Usa a funcao auxilir str_so_letras para
    tirar os espacos. De seguida, agrupa os caracteres em pares. Se forem iguais,
    coloca-se um X no meio e o segundo caracter passa ao proximo par. Se o
    houver um caracter sozinho num par (o ultimo), e adicionado tambem um X a
    seguir a ele'''
    mens_sl = str_so_letras(mens)
    def digramas_rec(mens):
        if mens == "":
            return ""
        elif len(mens) == 1: #sozinho no par
            return mens + "X"
        else:
            par = mens[0:2]
            if par[0] + par[0] == par: #par composto por caracteres iguais
                return par[0] + "X" + digramas(mens[1:])
            else:
                return par + digramas(mens[2:])
    return digramas_rec(mens_sl)

def procura_pos(l, chave):
    '''Recebe um caracter e uma chave e devolve a posicao desse caracter na
    chave'''
    for lin in range( len(chave) ):#procura por linhas
        for col in range( len(chave[lin]) ):#procura em cada coluna
            if ref_chave(chave, faz_pos(lin, col)) == l: #se encontrar
                return faz_pos(lin, col)
#figura
def figura(digrm, chave):
    '''Recebe uma cadeia de dois caracteres e uma chave e, usando a funcao auxiliar
    procura_pos, devolve a posicao de cada um dos caracteres na chave. Testa tambem
    se estao na mesma linha ('l'), na mesma coluna('c'), ou nenhum deles,
    formando um retangulo na chave ('r')'''
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
    '''Recebe um inteiro de 0-4 e incrementa-o ou decrementa-o consoante recebe
    1 ou -1 no segundo argumento. Se passar de 4 para a frente, volta a 0. E se
    passar de 0 para tras, passa para 4.'''
    variacao = indice + inc
    return variacao % 5

#codifica_l
def codifica_l(pos1, pos2, inc):
    '''Recebe duas posicoes e um incremento (1 ou -1) correspondente a querermos
    as posicoes encriptadas ou desencriptadas. Como as posicoes estao na mesma
    linha, apenas somamos o incremento a coluna para encriptar ou desencriptar.
    Usa-se a funcao auxiliar codifica_uni para quando passa dos limites [0-4].
    Retorna as duas posicoes encriptadas/desencriptadas.'''
    pos1_cod = faz_pos( linha_pos(pos1), codifica_uni(coluna_pos(pos1), inc) )
    pos2_cod = faz_pos( linha_pos(pos2), codifica_uni(coluna_pos(pos2), inc) )
    return (pos1_cod, pos2_cod)

#codifica_c
def codifica_c(pos1, pos2, inc):
    '''Recebe duas posicoes e um incremento (1 ou -1) correspondente a querermos
    as posicoes encriptadas ou desencriptadas. Como as posicoes estao na mesma
    coluna, apenas somamos o incremento a linha para encriptar ou desencriptar.
    Usa-se a funcao auxiliar codifica_uni para quando passa dos limites [0-4].
    Retorna as duas posicoes encriptadas/desencriptadas.'''
    pos1_cod = faz_pos( codifica_uni(linha_pos(pos1), inc), coluna_pos(pos1) )
    pos2_cod = faz_pos( codifica_uni(linha_pos(pos2), inc), coluna_pos(pos2) )
    return (pos1_cod, pos2_cod)

#codifica_r
def codifica_r(pos1, pos2):
    '''Recebe duas posicoes que nao estao nem na mesma linha nem na mesma coluna,
    e devolve as posicoes resultantes de trocar as colunas de uma pelas da outra,
    correspondendo aos outros cantos do retangulo que as posicoes fariam na chave.'''
    pos1_cod = faz_pos( linha_pos(pos1), coluna_pos(pos2) )
    pos2_cod = faz_pos( linha_pos(pos2), coluna_pos(pos1) )
    return (pos1_cod, pos2_cod)

#codifica_digrama
def codifica_digrama(digrm, chave, inc):
    '''Recebe um digrama composto por dois caracteres, uma chave e um incremento,
    correspondente a se queremos encriptar ou desencriptar. Verifica que figura
    eh que os caracteres fazem na chave, atraves da funcao figura e, consoante
    isto, evoca cada uma das funcoes codifica_l, codifica_c e codifica_r para
    encontrar as posicoes codificadas/descodificadas. Apos obter estas posicoes,
    usa a funcao ref_chave para procurar os caracteres que estao em casa uma
    destas posicoes da chave, devolvendo-os.'''
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
    '''Recebe uma cadeia de caracteres mens, uma chave e um incremento, consoante
    queremos encriptar ou desencriptar. Vai transformar a mensagem em pares,
    atraves da funcao digramas e, usa a funcao codifica_digramas para codificar
    cada par, retornando a mensagem encriptada/desencriptada no final.'''
    mens_cod = ""
    digrms = digramas(mens)
    for par in range(0, len(digrms), 2): #Salta de 2 em 2
        dig = digrms[par] + digrms[par + 1]
        mens_cod = mens_cod + codifica_digrama(dig, chave, inc)
    return mens_cod