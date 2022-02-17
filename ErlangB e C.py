--- number speller ----
a = {1:'um',2: 'dois',3 : 'três',4 : 'quatro',5 : 'cinco',6: 'seis',7: 'sete',8: 'oito',9: 'nove',10:'dez',11: 'onze',12: 'doze',13: 'treze',14: 'quatorze',15: 'quinze',16: 'dezesseis',17: 'dezessete',18: 'dezoito',19: 'dezenove',20: 'vinte',30: 'trinta', 40:'quarenta',50:'cinquenta',60: 'sessenta',70:'setenta',80:'oitenta',90:'noventa',100:'cem'}

def spell(num):
    if num <= 19 or num in (20,30,40,50,60,70,80,90,100):
        return a.get(num)
    elif num <= 99:
        num1 = [x for x in str(num)]
        x = int(num1[0])*10
        y = int(num1[1])
        return f'{str(a.get(x))} e {str(a.get(y))}'

print(spell(98))

def fatorial(val1):
    a = int(val1)
    p = 1
    for i in range(1,a+1):
        p= p * i
    return p

from math import e

def fatorial(val1):
    a = int(val1)
    p = 1
    for i in range(1,a+1):
        p= p * i
    return p

# Probabilidade de Congestionamento - menor melhor
def erlangb(chamadas_hora,canais):
    A = chamadas_hora
    N = canais
    i = 0
    s = 0
    j = (A**N)/fatorial(N)
    for i in range(1,canais+1):
        s = s+(A**i)/(fatorial(i))
    return (j/s)*100
    
#Probabilidade da chamada ultrapassar o Nivel de Serviço e ser atendida
def erlangc_pw(chamadas_hora,agentes):
    A = chamadas_hora
    N = agentes
    y = 1
    x = ((A**N)/fatorial(N))*(N/(N-A))
    for i in range(1,agentes+1):
        y = y+(A**i)/(fatorial(i))
    Pw = x/(y+x)
    return Pw
    
#Nivel de Serviço
def nivelservico(chamadas_hora,agentes,tempo_corte_ns,TMO):
    A = chamadas_hora
    N = agentes
    targettime = tempo_corte_ns
    AHT = TMO
    SL = (1-(erlangc_pw(A,N)*e**(-((N-A)*(targettime/AHT)))))
    return SL

# TME do cliente na fila antes de ser atendido: TMO em segundos
def tme(chamadas_hora, agentes, TMO):
    A = chamadas_hora
    N = agentes
    AHT = TMO
    ASA = (((erlangc_pw(A,N))*(AHT))/(N-A))
    return ASA
    
# Porcentagem de ligações atendidas imediatamente
def lig_imed(chamadas_hora,agentes):
    A = chamadas_hora
    N= agentes
    immediateanswer = (1-erlangc_pw(A,N))*100
    return immediateanswer
    
#Ocupação maxima - preferível abaixo de 85%
def ocupacao(chamadas_hora,agentes):
    A = chamadas_hora
    N = agentes
    ocuppancy = (A/N)*100
    return ocuppancy
    
#Minoração por ausência - Abs + Folga + Feriados - Atestados / Normal entre 30% e 35%
def agentes_real(agentes,percentual_minoracao):
    N = agentes
    sh = percentual_minoracao
    Nreal = N / (1-sh)
    return Nreal

