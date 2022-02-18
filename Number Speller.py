# Desafio para codar uma função que retorna o nome por extenso do número inputado
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