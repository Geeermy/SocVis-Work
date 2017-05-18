
# coding: utf-8

# # Tutorial - Librería pymysql

# En este tutorial, aprenderemos lo básico sobre la librería pymysql. Para ello,
# es necesario conocer lo básico de Python y de los comandos disponibles en
# **MySQL**.
# Importante: La mayoría de estos ejemplos se hicieron con una base de datos
# existentes, llamada "sl_marketplace". Se recomienda reemplazarla por una que
# exista en sus computadores, e ir creando tablas con los comandos vistos en la
# parte final del tutorial para poder entender a fondo todas las funcionalidades
# expuestas en este documento.


# En primer lugar, importamos la librería (que debe ser instalada previamente).
import pymysql # Librería para trabajar desde Python con bases de datos MySQL


# Ahora, nos conectamos con nuestra base de datos. En este caso, asumimos que se tiene una base de datos **local**. Todos los valores, en este caso, son estándar, salvo por "db", que corresponde al nombre de la base de datos utilizada para la realización de este tutorial. Notar que passwd="" ya que en nuestra configuración no tenemos introducida una contraseña.
connection = pymysql.connect(host="localhost", port=3306, user="root",
                             passwd="", db="sl_marketplace")


# Ahora, creamos el cursor. Este corresponde al iterador de las tablas. A través
# de él, conseguimos las filas de las tablas que consultamos.
cursor = connection.cursor()


# Ahora, hacemos el uso del método execute. Este es el que nos permitirá ejecutar nuestras consultas. Haremos uso de una tabla existente en la base de datos de prueba, llamada "stores" para ejemplificar el comando.
cursor.execute("SELECT * FROM stores LIMIT 5;")


# También se puede pasar la consulta a través de una variable. En este caso, la
# variable "query".
query = "SELECT * FROM stores LIMIT 5;"
cursor.execute(query)

# Para revisar las filas de la consulta, hacemos uso del método fetchall.
# Este nos retorna la lista de todas las filas. Notar que, en este caso, las
# filas corresponden a una tupla, por lo que no se pueden editar.
for row in cursor.fetchall():
    print(row)

# También podemos iterar haciendo uso de fetchone, que básicamente retorna la
# primera fila de la consulta, y pasa a la siguiente.
cursor.execute(query) # Ejecutamos la consulta de nuevo.
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()


# Por otra parte, está el comando fetchmany, que retorna solo la cantidad de
# filas que deseamos.
cursor.execute(query) # Ejecutamos la consulta de nuevo.
for row in cursor.fetchmany(size = 3):
    print(row)

# Variando la consulta, el tamaño de nuestra fila varía, naturalmente.
cursor.execute("SELECT store_id FROM stores LIMIT 5;") # Seleccionamos solo una
                                                       # columna.
for row in cursor.fetchall():
    print(row)


# También podemos seleccionar valores directamente desde los índices de la tupla
# resultante.
# Dos columnas.
cursor.execute("SELECT store_id, number_of_items FROM stores LIMIT 5;") 
for row in cursor.fetchall():
    print(row[1]) # Nos quedamos con la segunda.


# Otro beneficio, es que con pymysql también podemos crear y modificar tablas.
# A continuación, un ejemplo práctico.
# Tabla de dos columnas: val1 (numérico) y val2 (caracteres).
# Notar que CHARSET hará que no tengamos problemas con letras del español
# (como la ñ).
cursor.execute("CREATE TABLE testing (val1 int, val2 varchar(128)) "
               "ENGINE=InnoDB DEFAULT CHARSET=latin1;")
# Pasamos los valores en forma de tuplas.
values1 = (1,"Hola, ")
values2 = (2,"mundo!")
cursor.execute("INSERT INTO testing VALUES (%s,%s);",values1)
cursor.execute("INSERT INTO testing VALUES (%s,%s);",values2)

# Para que las modificaciones sean visualizables en la base de datos, es
# necesario que guardemos los cambios realizados. Por eso, a través de la
# variable "connection" creada en un comienzo, ejecutamos el commando commit.
connection.commit()


# Verificamos que todo se haya creado como lo esperábamos, a través de
# consultas, y un ejemplo práctico que muestra la utilidad que otorga Python
# para trabajar con bases de datos.
cursor.execute("SELECT * FROM testing;")
result = ""
for row in cursor.fetchall():
    result += row[1]
print(result)


# Ahora, modificaremos las tuplas y revisaremos el resultado.

# Otra forma de insertar valores en strings (ojo con el detalle de las comillas
# simples para introducir el valor de los caracteres).
cursor.execute("UPDATE testing SET val2 = '{}' "
               "WHERE val1 = 1;".format("Hello, "))
cursor.execute("UPDATE testing SET val2 = '{}' "
               "WHERE val1 = 2;".format("world!"))
connection.commit() # Guardamos los cambios.
# Vemos el resultado.
cursor.execute("SELECT * FROM testing;")
result = ""
for row in cursor.fetchall():
    result += row[1]
print(result)


# Finalizaremos este tutorial con la eliminación de la tabla creada
# recientemente.
cursor.execute("DROP TABLE testing;")
connection.commit()

# Revisamos que, efectivamente, se eliminó.
try:
    cursor.execute("SELECT * FROM testing;")
except:
    # Error - la tabla ya no existe.
    print("¡Tabla eliminada correctamente!")

