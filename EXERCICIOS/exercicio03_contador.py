'''
EXERCÍCIO 3
Crie um programa que:
1. Conte de 1 até 20.
2. Não mostre os números 5, 6 e 7.
3. Quando chegar no 15,
   encerre o programa.
Pratique:
- while
- +=
- continue
- break
- if
'''

start = 0
end = 20

while start <= end:
    
    start += 1

    if start >= 5 and start <= 7:
        continue

    print(start)   

    if start == 15:
        break