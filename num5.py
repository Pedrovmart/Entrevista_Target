import string
palavra = input('Digite a palavra: ')
reversa =[]
for i in range(-1, -len(palavra)-1, -1):
    reversa.append(palavra[i])
    
print(''.join(reversa))    
    
    
    