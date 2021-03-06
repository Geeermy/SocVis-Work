# Script para mostrar el uso de ggplot2 a trav�s de un ejemplo con Second Life.
# Datos capturados desde: https://marketplace.secondlife.com/
# 
# @date August 5, 2016
# @author Germ�n Contreras

# Comenzamos con la implementaci�n de las librer�as a utilizar

# Ejecutar si es que no lo hemos instalado.
# install.packages("ggplot2") 

library("ggplot2")

# Un peque�o ejemplo del manejo de datos.

# Notar que c(x1,x2,...,xn) corresponde a un vector de n variables.
charlistas = data.frame(
                        charlista = c("Denis","German","Daniela","Vicente"),
                        charla = c("R 101", "ggplot2", "Dashboards", "MatplotLib"),
                        asistentes = c(50,39,47,42)
                        )
charlistas$charlista
charlistas$charlista[3]
charlistas[2]

# Ahora, hacemos la lectura del conjunto de datos a utilizar.
# Recordar cambiar la direcci�n para que coincida con la de ustedes.

# Primer conjunto de datos
ejemplo1 = read.csv(file = "C:/Users/German/ggplot2/Data1.csv", row.names = NULL)

# Segundo conjunto de datos
ejemplo2 = read.csv(file = "C:/Users/German/ggplot2/Data2.csv", row.names = NULL)

# ======================================================================================
# NOTA: Otra forma de hacerlo es cambiando el directorio de trabajo (Working Directory).
# Para ello, ejecutan el siguiente comando:
# setwd("La/ruta/de/mi/directorio")
# De esta forma, podemos poner solo los nombres de los archivos, en vez de su ruta.
# En este caso particular, tendr�a que ser: setwd("C:/Users/German/ggplot2")
# ======================================================================================

# Partimos trabajando con el primer ejemplo, para poder elaborar nuestro gr�fico de forma 
# incremental.

# Histograma b�sico, con eje X rating y eje Y la cantidad de tiendas con dicho rating.
# geom_histogram es el que hace que el tipo de gr�fico sea un histograma.
plot = (ggplot(data = ejemplo1, aes(x = rating))
       + geom_histogram())
plot

# Vamos a editar la informaci�n b�sica. Cambiaremos los nombres de los ejes y le daremos un
# nombre a nuestro gr�fico.
plot = (ggplot(data = ejemplo1, aes(x = rating))
        + geom_histogram()
        + xlab("Rating")
        + ylab("Cantidad de tiendas")
        + ggtitle("Frecuencia de tiendas por rating"))
plot
# xlab: Nombre de la etiqueta del eje x.
# ylab: Nombre de la etiqueta del eje y.
# ggtitle: T�tulo del gr�fico.

# Ahora, le a�adiremos estilo al gr�fico.
# Haremos que cada barra posea un color similar al del logo de Second Life, adem�s de a�adirle
# un marco. Por otra parte, aumentaremos el ancho de nuestras barras, adem�s de alinearlas con
# su respectiva etiqueta.
plot = (ggplot(data = ejemplo1, aes(x = as.numeric(rating)))
        + geom_histogram(colour = "darkslategray", fill = "darkslategray4", 
                         binwidth = 0.5)
        + scale_x_discrete(limits = c(1,5), expand = c(0.05,0.05))
        + xlab("Rating")
        + ylab("Cantidad de tiendas")
        + ggtitle("Frecuencia de tiendas por rating"))
plot
# colour corresponde al borde, y fill al relleno de las barras.
# binwidth es el ancho de cada barra, y origin es el origen de estas.
# scale_x_discrete asegura que no quede espacio inutilizado a los costados del gr�fico, esto
# a trav�s de limits (limita los valores) y expand (que finalmente permite dar la cantidad de
# espacio libre entre los bordes deseada).

# =========================================================================
# NOTA: Pueden encontrar los nombres de los colores aqu�: 
# http://research.stowers-institute.org/efg/R/Color/Chart/ColorChart.pdf
# =========================================================================

# Ahora, en vez de tener en el eje Y la cantidad de tiendas, tendremos la densidad de tiendas.
# Adem�s, pondremos sobre el histograma el gr�fico de la densidad.
plot = (ggplot(data = ejemplo1, aes(x = as.numeric(rating), y = ..density..))
        + geom_histogram(colour = "darkslategray", fill = "darkslategray4", 
                         binwidth = 0.5)
        + geom_density(colour = "darkturquoise")
        + scale_x_discrete(limits = c(1,5), expand = c(0.05,0.05))
        + xlab("Rating")
        + ylab("Densidad de tiendas")
        + ggtitle("Frecuencia de tiendas por rating"))
plot

# Si no quisi�ramos perder la frecuencia obtenida, podemos dejarla sobre cada barra.
plot = (ggplot(data = ejemplo1, aes(x = as.numeric(rating), y = ..density..))
        + geom_histogram(colour = "darkslategray", fill = "darkslategray4", 
                         binwidth = 0.5)
        + geom_density(colour = "darkturquoise")
        + geom_text(stat = "bin", aes(label = ..count..), vjust = -1, fontface = "bold",
                    colour = "darkslategray4")
        + scale_x_discrete(limits = c(1,5), expand = c(0.05,0.05))
        + xlab("Rating")
        + ylab("Densidad de tiendas")
        + ggtitle("Frecuencia de tiendas por rating"))
plot
# geom_text permite incluir texto sobre el gr�fico. Le damos como valor la frecuencia del
# histograma, con vjust hacemos que quede sobre la barra, y con fontface hacemos que el
# n�mero quede en negrita.

# Ahora, usaremos el segundo conjunto de datos, para poder mostrar m�ltiples datos a la vez.
# Estos datos ahora contienen un a�o. Veremos dos formas de visualizar esto.
plot = (ggplot(data = ejemplo2, aes(x = as.numeric(rating), y = ..density.., 
                                    fill = as.factor(year)))
        + geom_histogram(colour = "darkslategray", binwidth = 0.5)
        + scale_x_discrete(limits = c(0,5), expand = c(0.05,0.05))
        + xlab("Rating")
        + ylab("Densidad de tiendas")
        + ggtitle("Frecuencia de tiendas por rating"))
plot
# Ahora, usamos el relleno de las barras como un factor -> as.factor(year)
# Adem�s, con position = "dodge" hacemos que las barras queden separadas y no unas sobre las
# otras.


# Pasamos al otro m�todo.
plot = (ggplot(data = ejemplo2, aes(x = as.numeric(rating), y = ..density..))
        + geom_histogram(colour = "darkslategray", fill = "darkslategray4", 
                         binwidth = 0.5)
        + geom_density(colour = "darkturquoise")
        + scale_x_discrete(limits = c(0,5), expand = c(0.05,0.05))
        + xlab("Rating")
        + ylab("Densidad de tiendas")
        + ggtitle("Frecuencia de tiendas por rating")
        + facet_wrap(~ year))
plot
# facet_wrap nos permite hacer un gr�fico a partir de una cierta variable (por ejemplo, aqu�)
# hacemos cada grafico por a�o.

# Ahora, realizaremos un scatterplot simple, y visualizaremos m�s datos de a poco. Para estos
# casos utilizaremos los otros dos conjuntos de datos.
# Primero, el scatterplot base.
plot = (ggplot(data = ejemplo3, aes(x = sentiment, y = products))
        + geom_point(colour = "darkslategray4", alpha = 0.5, position = "jitter")
        + xlab("Sentimiento de los compradores")
        + ylab("N�mero de productos")
        + ggtitle("Gr�fico de dispersi�n - Sentimiento de compradores y Productos de tienda"))
plot