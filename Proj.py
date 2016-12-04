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
def gera_chave_linhas(l, mgc):
    if isinstance(l, tuple) and not len([car for car in l if (not isinstance(car,str))]) and len(l)==25 and isinstance(mgc, str):
        compact=()
        resto=()
        for car in range(len(mgc)):
                if mgc[car] not in compact:
                    compact = compact + (mgc[car],)
        for letra in range(len(l)):
                if l[letra] not in compact:
                    resto = resto + (l[letra],)
        return compact + resto

