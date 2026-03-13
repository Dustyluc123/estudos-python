#AULA 01

#1. inserção dos dados de placa do motor

#Potência Útil (Mecânica)
#Potência Útil (Mecânica)
PU = int(input('Insira o valor da potencia util em kw: '))
n = float(input('Insira o valor do rendimento do motor (de 0 a 1): '))

#2. Calculo de potencia ativa
# Rendimento: 
#n = PU / p
P = PU / n

print(f'A potencia ativa será de {P:.2f} W')