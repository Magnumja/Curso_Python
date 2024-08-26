print(12, 34)
print(56, 78)

# se quiser separar os números coloque literalmente o "sep", para dar espaçamento. 


print(56, 78, sep="-")
print(56, 78, sep='-')

# se quiser dar espaçamento pode tambem utilizar o \r\n (para windows mais antigos) e /n somente (para windows mais atuualizados)
# \r\n ---> CRLF
# \n ----> LF

print(12, 34, 1011, sep="-", end='\n##')
print(45, 54)