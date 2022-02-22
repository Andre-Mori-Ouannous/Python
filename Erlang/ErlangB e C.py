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