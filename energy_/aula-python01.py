
#Potência Útil (Mecânica)
#Potência Útil (Mecânica)
PU = int(input('Insira o valor da potencia util em kw: '))
n = float(input('Insira o valor do rendimento do motor (de 0 a 1): '))
FP = float(input('Insira o valor do fator de potência (de 0 a 1): '))
# Rendimento: 
#n = PU / p
# Potência Ativa (em Watss)
P = PU / n
# Potência Aparente (em Volt-Ampére)
S = P / FP
# Potência Reativa (em Volt-Ampére-Reativo)
Q = (S**2 - P**2)**(1/2)

print(f'A potencia ativa será de {P:.1f} W')
print(f'A potencia aparente será de {S:.1f} VA') 
print(f'A potencia reativa será de {Q:.1f} VAr')