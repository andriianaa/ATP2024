def menu():
    print("(1)-Calcular temperatura média")
    print("(2)-Guardar tabela meteorológica num ficheiro")
    print("(3)-Carregar tabela dum ficheiro")
    print("(4)-Calcular temperatura mínima")
    print("(5)-Calcular amplitude térmica")
    print("(6)-Calcular dia de precipitação máxima")
    print("(7)-Calcular dias de precipitação superiores ao limite desejado")
    print("(8)-Calcular máximo período de precipitação")
    print("(9)-Desenhar gráficos")
    print("(0)-Sair")
    return

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def medias(tabMeteo):
    res = []
    for data,tmin,tmax,precip in tabMeteo:
        res.append((data,(tmin+tmax)/2))
    return res

def guardaTabMeteo(t, fnome):
    f=open(fnome, "w")
    for data,tmin,tmax,precip in t:
        linha=f"{data[0]}::{data[1]}::{data[2]}::{tmin}::{tmax}::{precip}\n"
        f.write(linha)
    f.close()

    return len(t) 
guardaTabMeteo(tabMeteo1, "meteorologia.txt")

def carregaTabMeteo(fnome):
    res = []
    f=open(fnome)
    for linha in f:
        campos=linha.split('::')
        data=(int(campos[0]),int(campos[1]),int(campos[2]))
        res.append((data,float(campos[3]),float(campos[4]),float(campos[5])))
    f.close()
    return res

def minMin(tabMeteo):
    minima=tabMeteo[0][1]
    for _,tmin, *_ in tabMeteo[1:]:  ##usamos o _ para ignorar as variáveis que não usamos
        if tmin<minima:
            minima=tmin
    return minima

def amplTerm(tabMeteo):
    res = []
    for data,tmin,tmax,precip in tabMeteo:
        res.append((data,tmax-tmin))

    return res 

def maxChuva(tabMeteo):
    max_prec=tabMeteo[0][3]
    data_max=tabMeteo[0][0]
    for data,tmin,tmax,precip in tabMeteo[1:]:
        if precip>max_prec:
            max_prec=precip
            data_max=data

    return (data_max, max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    for data,tmin,tmax,precip in tabMeteo:
        if precip>p:
            res.append((precip,data))
    return res

def maxPeriodoChuva(tabMeteo, p):
    consecutivos=0
    contador=0
    for *_,precip in tabMeteo:
        if precip<p:
            contador=contador+1
        else:
            if consecutivos<contador:
                consecutivos=contador
            contador=0
    return consecutivos

import matplotlib.pyplot as plt
def grafTabMeteo(tabMeteo):
    datas = [f"{data[0]}/{data[1]}/{data[2]}" for data, _, _, _ in tabMeteo]
    temp_min = [tmin for _, tmin, _, _ in tabMeteo]
    temp_max = [tmax for _, _, tmax, _ in tabMeteo]
    precip = [precip for _, _, _, precip in tabMeteo]

    plt.figure(figsize=(12, 6))
    
    
    plt.subplot(2, 1, 1)
    plt.plot(datas, temp_min, label="Temperatura Mínima", color="blue", marker="o")
    plt.plot(datas, temp_max, label="Temperatura Máxima", color="red", marker="o")
    plt.xticks(rotation=45)
    plt.xlabel("Data")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperatura Mínima e Máxima ao Longo do Tempo")


    
    plt.subplot(2, 1, 2)
    plt.bar(datas, precip, color="cyan")
    plt.xticks(rotation=45)
    plt.xlabel("Data")
    plt.ylabel("Precipitação (mm)")
    plt.title("Precipitação ao Longo do Tempo")

    plt.tight_layout()
    plt.show()
    return


menu()
opcao = input("Escolha uma opção: ")
while opcao !="0":
        
    if opcao == "1":
        print(medias(tabMeteo1))   
    elif opcao == "2":
        guardaTabMeteo(tabMeteo1,"METEOROLOGIA.txt")   
    elif opcao == "3":
        tabMeteo2 = carregaTabMeteo("meteorologia.txt")
        print(tabMeteo2) 
    elif opcao == "4":
        print(minMin(tabMeteo1))  
    elif opcao == "5":
        print(amplTerm(tabMeteo1))
    elif opcao=="6":
        print(maxChuva(tabMeteo1))
    elif opcao=="7":
        p=int(input("Introduza um limite p:"))
        print(diasChuvosos(tabMeteo1,p))
    elif opcao=="8":
        p=float(input("Introduza o limite desejado:"))
        print(maxPeriodoChuva(tabMeteo1,p))
    elif opcao=="9":
        grafTabMeteo(tabMeteo1)
    else:
        print("Opção inválida, tente novamente.")
    menu()
    opcao = input("Escolha uma opção: ")
print("Obrigado, volte sempre!")
