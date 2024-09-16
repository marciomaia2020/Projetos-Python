a,b = 10,5
if a > b:
    print('a ({}) é maior que b ({}).'.format(a,b))
else:
    print('a ({}) é menor que b ({}).'.format(a,b) )

#NÃO FUNCIONA
print ("({}) é maior que ({})" if a > b else "({}) é maior que ({})".format(a,b))

#Usando o Método format
print("{} é maior que {}".format(a, b) if a > b else "{} é maior que {}".format(b, a))

#Usando f-strings (para Python 3.6+)
print(f"{a} é maior que {b}" if a > b else f"{b} é maior que {a}")


   