# AULA 11

# PRECEDÊNCIA DOS OPERADORES / 
# ORDEM DE RESOLUÇÃO DO CÓDIGO
# COMEÇA SEMPRE PELO (), O MAIS INTERNO PRIMEIRO

# 1. (N + N)
# 2. **
# 3. *  /  //  %
# 4. +  -

# 
conta_1 = 1 + 1 ** 5 + 5 # = 7
print(conta_1) 

#
conta_2 = (1 + 1) ** (5 + 5) # = 1024
print(conta_2)

#
conta_3 = ((1 + 1) ** 5) + 5 # = 37
print(conta_3)