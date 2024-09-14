# 1.Conversion tipo de datos
#enteros
numero = 14
print ("numero:",numero)
#decimales
numero1=14.5
print("numero decimal:",numero1)
#cadenas
nombre="edward david catamuscay"
print("nombre:",nombre)

# 2.Multilíneas de cadenas
ej=("ese una cadena que puede incluir varias lienas de comando es decir:"
    "puede mostrar varias variables en una misma linea que se imprima: ")
print(ej+nombre)

# 3.Función len()
ej1= "estudio ingenieria en sistemas"
print(len(ej1))

# 4.Sub cadenas
#Obtener los primeros n caracteres de una cadena
ej2="grupo1"
nume=5
print("imprime los primeros 5 caracteres de la palabra",ej2[:nume])
#Obtener los caracteres de en medio de una cadena.
ej3="la clase se llama electiva profesional"
nu=12
num=19
print("imprime las letras de enmedio de una cadena: ",ej3[nu:num])
#Obtener los últimos n caracteres de una cadena.
ej4="vamos a terminar el primer corte"
n=5
print("imprime los  ultimos caracteres de una cadena: ",ej4[-n:])
#Función upper()
ej5="quiero especializarme en desarrollo de software"
print(ej5.upper())
#Funcion upper
ej6="APENAS TERMINE LA CARRERA"
print(ej6.lower())
#Mutilineas de cadenas de caracteres
ej7='''este comando permite crear cadenas
sin improtar los esacios que ocupe

'''
print(ej7)
#Funcion strip()
ej8="####funcion strip####"
print(ej8.strip("#"))
#Función replace()
ej9="electiva profesional "
print(ej9.replace("profesional","1"))
#Función split()
ej10="electiva,profesional,2"
print(ej10.split(","))
#Formato de cadenas F-String
hermano="juan jose"
cadena=f"hola me llamo{nombre},tengo un hermano llamado {hermano}"
print(cadena)


