# AULA 14

# FUNÇÃO .FORMAT
a = 'A'
b = 'B'
c = 1.1
string = 'a:{} b={} c={:.2f}'
formato = string .format(a, b, c)
print(formato) 
print('----')
# Nesse formato, as {} sempre serão usadas em ordem,
# começando do 0.
#--------------------------------------------------#

# ENUMERAR INDICES
a = 'A'
b = 'B'
c = 1.1
string = 'a:{0} b={1} b={1} c={2:.2f}'
formato = string .format(a, b, c)
print(formato)
print('----')
# Aqui você pode enumerar as chaves{}, assim você decide a ordem.
#---------------------------------------------------#

# PARAMETRO NOMEADO - EX: (nome1, nome 2...)
a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} b={nome2} c={nome3:.2f}'
formato = string .format(nome1=a, nome2=b, nome3=c)
print(formato)
print('----')
# Aqui voce consegue nomear os parametros.
# (nome3=c) (nome3: parametro. c: argumento)
