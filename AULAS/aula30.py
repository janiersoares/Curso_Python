# AULA 30

# VÁRIAVEIS, CONSTANTES E COMPLEXIDADE DE CÓDIGO.
'''
CONSTANTE(em capslock) = "váriaveis" que não vão mudar.
Muitas condições no mesmo if(ruim).
        <- quanto mais afastado da barra lateral, mais complexo.
        Complexidade demais = (ruim).

velocidade = 61 # velocidade atual do carro.
local_carro = 90 # local em que o carro está na estrada.

RADAR_1 = 60 # velocidade máxima do radar 1.
LOCAL_1 = 100 # local do primeiro radar.
RADAR_RANGE = 1 # a distancia onde o radar pega.

if velocidade > RADAR_1:
    print(f'Passou acima da velocidade no radar 1.')
    
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print(f'Carro mulado no radar 1.')
'''
# LIMPANDO O CÓDIGO

velocidade = 62 # velocidade atual do carro.
local_carro = 90 # local em que o carro está na estrada.

RADAR_1 = 60 # velocidade máxima do radar 1.
LOCAL_1 = 100 # local do primeiro radar.
RADAR_RANGE = 1 # a distancia onde o radar pega.

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_radar1

if velocidade_carro_passou_radar1:
    print(f'Passou acima da velocidade no radar 1.')
    
if carro_passou_radar1:
    print(f'Carro passou no radar 1.')

if carro_multado_radar1:
    print(f'Carro multado no radar 1.')