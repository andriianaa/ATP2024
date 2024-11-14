#TPC1
##a)
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = []
for elemento in lista1:
    if elemento not in lista2:
        ncomuns.append(elemento)

for elemento in lista2:
    if elemento not in lista1:
        ncomuns.append(elemento)

print(ncomuns)

##b)
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = []
for palavra in texto.split():
    if len(palavra)>3:
        lista.append(palavra)

print(lista)

##c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = []
i=1
for palavra in lista:
    listaRes.append((i,palavra))
    i=i+1

print(listaRes)



#TPC2
##a)
def strCount(s, subs):
    count=0
    i=0

    while i <=len(s)-len(subs):
        if s[i:i+len(subs)]==subs:
            count=count+1
            i=i+len(subs)
        else:
            i=i+1
    return count

print(strCount("catcowcat", "cat")) # --> 2
print(strCount("catcowcat", "cow")) # --> 1
print(strCount("catcowcat", "dog")) # --> 0

##b)
def produtoM3(lista):
    ordenaLista=sorted(lista)
    menor1, menor2, menor3 = ordenaLista[0], ordenaLista[1], ordenaLista[2]
    produto=menor1*menor2*menor3
    return  produto

print(produtoM3([12,3,7,10,12,8,9]))

##c)
def reduxInt(n):
    while n>=10:
        nStr=str(n)
        soma=0

        for digito in nStr:
            intDigito=int(digito)
            soma=soma+intDigito
        n=soma
    return n
print(reduxInt(38))
print(reduxInt(777))

##d)
def myIndexOf(s1, s2):
    for i in range(len(s1)-len(s2)+1):
        if s1[i:i+len(s2)]==s2:
            return i
    return -1

print(myIndexOf("Hoje está um belo dia de sol!", "belo"))  
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))



#TPC3-Rede Social
MyFaceBook = [
    {'id': 'p1', 'conteudo': 'A tarefa de avaliação é talvez a mais ingrata...', 'autor': 'jcr', 'dataCriacao': '2023-07-20', 'comentarios': [{'comentario': 'Completamente de acordo...', 'autor': 'prh'}, {'comentario': 'Mas há quem goste...', 'autor': 'jj'}]},
    {'id': 'p2', 'conteudo': 'Outro post...', 'autor': 'xyz', 'dataCriacao': '2023-07-21', 'comentarios': [{'comentario': 'Comentário 1', 'autor': 'abc'}]},
    {'id': 'p3', 'conteudo': 'Post sobre Python.', 'autor': 'jcr', 'dataCriacao': '2023-07-22', 'comentarios': [{'comentario': 'Muito interessante!', 'autor': 'xyz'}]}
]


def quantosPost(redeSocial):
    return len(redeSocial)
print(quantosPost(MyFaceBook)) 

def postsAutor(redeSocial, autor):
    listapostsAutor=[]
    for post in redeSocial:
        if post["autor"]==autor:
            listapostsAutor.append(post)
    return listapostsAutor
print(postsAutor(MyFaceBook, 'jcr'))

def autores(redeSocial):
    listaAutores=[]
    for post in redeSocial:
        listaAutores.append(post["autor"])

    listaAutores.sort()
    return listaAutores
print(autores(MyFaceBook))

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    
    maiorId=0
    for post in redeSocial:
        numeroId=int(post["id"][1:])
        if numeroId>maiorId:
            maiorId=numeroId
    id=f"p{maiorId+1}"
    novoPost={
        "id":id,
        "conteudo":conteudo,
        "autor":autor,
        "dataCriacao":dataCriacao,
        "comentarios":comentarios
    }

    redeSocial.append(novoPost)
    return redeSocial

nova_rede = insPost(MyFaceBook, 'Novo post sobre programação!', 'abc', '2023-11-13', [{'comentario': 'Muito bom!', 'autor': 'jcr'}])
for post in nova_rede:
    print(post)

def remPost(redeSocial, id):
    novaRede=[]
    for post in redeSocial:
        if post["id"]!=id:
            novaRede.append(post)
    return novaRede

nova_rede = remPost(MyFaceBook, 'p2')
for post in nova_rede:
    print(post)

def postsPorAutor(redeSocial):
    distribuicao={}
    for post in redeSocial:
        autor=post["autor"]
        if autor not in distribuicao:
            distribuicao[autor]=[]
        distribuicao[autor].append(post)
    return distribuicao
distribuicao = postsPorAutor(MyFaceBook)

for autor, posts in distribuicao.items():
    print(f"Autor: {autor}")
    for post in posts:
        print(f"  {post['id']}: {post['conteudo']}")

def comentadoPor(redeSocial, autor):
    postsComentados=[]
    for post in redeSocial:
        comentou=False
        for comentario in post["comentarios"]:
            if comentario["autor"]==autor:
                comentou=True
        
        if comentou:
            postsComentados.append(post) 
    return postsComentados

posts_jcr_comentados = comentadoPor(MyFaceBook, 'jcr')

for post in posts_jcr_comentados:
    print(f"Post ID: {post['id']} - {post['conteudo']}")


