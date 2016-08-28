#Classificação de sinais utilizando matriz euclidiana
#autor Diego Silva Caldeira Rocha

import numpy as np

a=  np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]])
#c=  np.array([[5,2,9]])
c=np.zeros((3))
#print(a)
#print (c)
#np.insert(a,c)

#a=np.vstack((a,c))
#a=np.concatenate((a, c),axis=0)
#print(a)

AtSig=np.zeros((21))

MS0=np.empty((21))#matriz com amostra dos atributos do sinal tipo 0 
MS1=np.empty((21))#MS1#matriz com amostra dos atributos do sinal tipo 1
MS2=np.empty((21)) #MS2#matriz com amostra dos atributos do sinal tipo 2
ts0=0
ts1=0
ts2=0
ref_arquivo = open("waveform.data", "r")
ref_arqsaid = open("result.data", "w")
i=-1;
for line in range(1,2201):
    value=ref_arquivo.readline()
    i=i+1
    AtSig[i] =float(value)   
    if (i==20):
        id=int(ref_arquivo.readline())
        i=-1;
        if (id==0):
            ts0=ts0+1
            MS0=np.vstack((MS0,AtSig))
        elif(id==1):
            ts1=ts1+1
            MS1=np.vstack((MS1,AtSig))
        elif(id==2):
            ts2=ts2+1
            MS2=np.vstack((MS2,AtSig))
        

MS0=np.delete(MS0, 0, 0)
MS1=np.delete(MS1, 0, 0)
MS2=np.delete(MS2, 0, 0)
erro=0;
acerto=0;

#print(MS1)
while (value!=''):
    CtSig=np.zeros((21))
    i=-1;
    for line in range(0,21):
        value=ref_arquivo.readline()
        i=i+1
        if (value==''):
            break
        CtSig[i] =float(value) 
        if (i==21):
            id=int(ref_arquivo.readline())
            i=-1;

    best=float('inf')
    classe=3
    #comparando com sinal da classe 0

    for aux in range(0,ts0):
        R=MS0[aux]-CtSig #distancia euclidiana entre os atributos do sinal
        R=R*R
        R=R**0.5
        if(best>R.mean()):
            best=R.mean()#calculando a média das distancia eucldiana
            classe=0

    #comparando com sinal da classe 1

    for aux in range(0,ts1):
        R=MS1[aux]-CtSig #distancia euclidiana entre os atributos do sinal
        R=R*R
        R=R**0.5
        if(best>R.mean()):
            best=R.mean()#calculando a média das distancia eucldiana
            classe=1

    #comparando com sinal da classe 2

    for aux in range(0,ts2):
        R=MS2[aux]-CtSig #distancia euclidiana entre os atributos do sinal
        R=R*R
        R=R**0.5
        if(best>R.mean()):
            best=R.mean()#calculando a média das distancia eucldiana
            classe=2
    if (classe==id):
        acerto=acerto+1
    else:
        erro=erro+1
    
    ref_arqsaid.write('classe de sinal:'+str(classe)+'atributos:'+str(CtSig)+'\n')

value=ref_arquivo.readline()
print(value)
##
##
##print(AtSig)
##print(CtSig)
##
##
##R=AtSig-CtSig
##
##
##print(R)
##
##print(R.mean())
##
ref_arqsaid.write('acertos:'+str(acerto)+'erro:'+str(erro)+'total:'+str((acerto/(acerto+erro)*100)))




ref_arquivo.close()
ref_arqsaid.close()
