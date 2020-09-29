# Este es un progra,a que lee e imprime en orden

#Declaras abrir el txt y utilizas un metodo para leerlo

f = open ('holamundo.txt','r')
mensaje = f.read()

#Guarda en my_str el mensaje

my_str = (mensaje)


# Entra como una entrada


# Entra la oracion como una cadena y la separa por espacios en blanco

words = my_str.split()


# Aqui ordena la lista mediante sort

words.sort()


# Imprimes el metodo


print("La oracion en orden es:")

for word in words:

   print(word)
