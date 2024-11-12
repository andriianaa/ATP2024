def menu():
    print("(1)-Criar uma turma")
    print("(2)-Inserir um aluno na turma")
    print("(3)-Listar turma")
    print("(4)-Consultar um aluno por id")
    print("(5)-Guardar a turma em ficheiro")
    print("(6)-Carregar uma turma dum ficheiro ")
    print("(0)-Sair")
    return

turma=[]

def criarTurma():
    turma=[]
    print("Nova turma criada.")
    return

def inserirAluno():
    nome=input("Introduza o nome do aluno:")
    id=input("Introduza o id do aluno:")
    notas=[ 
        float(input("Introduza a nota do TPC:")),
        float(input("Introduza a nota do Projeto:")),
        float(input("Introduza a nota do Teste:")),
    ]
    aluno=(nome,id,notas)
    turma.append(aluno)
    print(f"Aluno {nome} adicionado à turma.")
    return

def listarTurma():
    for aluno in turma:
        print(f"Nome:{aluno[0]}, ID:{aluno[1]}, Notas:TPC={aluno[2][0]}, Projeto={aluno[2][1]}, Teste={aluno[2][2]}")
    return

def consultarAluno():
    id=input("Introduza o ID do aluno a consultar:")
    encontrado=False
    for aluno in turma:
        if aluno[1]==id:
            print(f"Nome:{aluno[0]}, ID:{aluno[1]}, Notas:TPC={aluno[2][0]}, Projeto={aluno[2][1]}, Teste={aluno[2][2]}")
            encontrado=True
    if not encontrado:
        print("ID inválido")  
    return

def guardaremFicheiro(turma,fnome):
    file = open(fnome,"w")
    for aluno in turma:
        file.write(f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n")
    file.close()  
    print(f"Turma guardada em {fnome} com sucesso.")
    return 

def carregardeFicheiro(fnome):
    turma=[]
    file = open(fnome,"r")
    for linha in file:
        partes = linha.split(',')
        nome = partes[0]
        id = partes[1]
        notas = [float(partes[2]), float(partes[3]), float(partes[4])]
        aluno = (nome, id, notas)
        turma.append(aluno)
    file.close()
    return turma


menu()
opcao = input("Escolha uma opção: ")
while opcao !="0":
        
    if opcao == "1":
        criarTurma()    
    elif opcao == "2":
        inserirAluno()   
    elif opcao == "3":
        listarTurma()   
    elif opcao == "4":
        consultarAluno()   
    elif opcao == "5":
        guardaremFicheiro(turma,"turma.txt") 
    elif opcao=="6":
        carregardeFicheiro("turma.txt")
        print(turma)
    else:
        print("Opção inválida, tente novamente.")
    menu()
    opcao = input("Escolha uma opção: ")
print("Obrigado, volte sempre!")