# coding: utf-8

# # Tutorial - Análisis de Sentimiento con SentiStrength y TextBlob

# En este tutorial, aprenderemos el uso básico de las librerías SentiStrength y
# TextBlob. Para ello, es necesario conocer el manejo básico de Python. 
# Antes de partir, es necesario descargar la librerías requeridas. 
# ### Instalar SentiStrength
# Para SentiStrength, es necesario seguir las instrucciones que se encuentran en
# el siguiente enlace: http://sentistrength.wlv.ac.uk/#Download
# ### Instalar TextBlob
# Se puede hacer con el comando pip install, como se detalla aquí:
# http://textblob.readthedocs.io/en/dev/install.html
# Ahora, partimos por importar las librerías.

# Importamos la librería necesaria para poder usar SentiStrength (programa en
# Java).
import subprocess, shlex
# Importamos la librería de TextBlob
from textblob import TextBlob


# ## Usando SentiStrength
# 
# Para SentiStrength, utilizamos la función que provee la misma página para
# hacer uso del programa en Python.

# Función para obtener el sentimiento del comentario haciendo uso de
# SentiStrength.
# Alec Larsen - University of the Witwatersrand, South Africa, 2012.
def RateSentiment(sentiString):
    # Se abre un subproceso usando shlex para obtener el string de la línea de
    # comando en el formato correcto de lista de argumentos.
    p = subprocess.Popen(shlex.split("java -jar C:/SentiStrength.jar stdin sentidata C:/SentStrength_Data/"),
                         stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # Se comunica por stdin el string a ser medido. Todos los espacios son
    # reemplazados con el símbolo +.
    stdout_text, stderr_text = p.communicate(sentiString.replace(" ","+").encode())
    # Removemos los espacios entre el rating positivo y negativo. Ejemplo: 1    -5 -> 1-5
    stdout_text = stdout_text.decode().rstrip().replace("\t","")
    return stdout_text


# Ahora, haremos uso de dos strings de ejemplo para obtener sus sentimientos:
# Uno evidentemente positivo, y otro evidentemente negativo.

# Te amo tanto, cariño.
string_1 = "I love you so much, darling."
# Realmente te odio, idiota.
string_2 = "I really hate you, stupid."

# Obtenemos los sentimientos con la función definida previamente.
sentiment_1 = RateSentiment(string_1)
sentiment_2 = RateSentiment(string_2)

# Ahora, abusaremos del formato (valores de 1 a 5 y -1 a -5) para obtener los valores.
positive_1 = int(sentiment_1[0])
negative_1 = int(sentiment_1[1:])
positive_2 = int(sentiment_2[0])
negative_2 = int(sentiment_2[1:])

# Mostramos los resultados.
print('========== SENTISTRENGTH ==========')
print('Resultados del string "{0}":\nSentimiento positivo: {1}\nSentimiento negativo: {2}'.format(string_1, positive_1,
                                                                                                    negative_1))
print('Resultados del string "{0}":\nSentimiento positivo: {1}\nSentimiento negativo: {2}'.format(string_2, positive_2,
                                                                                                    negative_2))


# Podemos ver que el programa nos entrega resultados razonables, basándonos en
# el texto que pusimos. 
# ## Usando TextBlob
# Ahora, haremos uso de TextBlob en los mismos ejemplos que vimos antes. Hay que
# notar que el manejo, sin embargo, es un poco diferente.

# Creamos dos objetos de clase "TextBlob" basados en los ejemplos anteriores.
textblob_1 = TextBlob(string_1)
textblob_2 = TextBlob(string_2)

# Veamos los sentimientos. TextBlob los separa por polaridad (varía entre -1 y
# 1) y subjetividad (varía entre 0 y 1).
print('========== TEXTBLOB ==========')
print('Resultados del string "{0}":\nPolaridad: {1}\nSubjetividad: {2}'.format(string_1,textblob_1.sentiment.polarity,
                                                                               textblob_1.sentiment.subjectivity))
print('Resultados del string "{0}":\nPolaridad: {1}\nSubjetividad: {2}'.format(string_2,textblob_2.sentiment.polarity,
                                                                               textblob_2.sentiment.subjectivity))


# Si bien TextBlob se utiliza para obtener sentimiento, tiene muchas más
# funcionalidades. Un método útil es la traducción de texto (lo que realiza a
# partir de Google Translate).

# Traduzcamos los textos, para empezar.
print("{0} ===> En español ===> {1}".format(string_1,
      str(textblob_1.translate(from_lang="en", to="es"))))
print("{0} ===> En español ===> {1}".format(string_2,
      str(textblob_2.translate(from_lang="en", to="es"))))

# ¿Podríamos entonces tomar un texto en español y obtener su sentimiento?
# Veamos.

testing_1 = "Te amo, eres el mejor."
testing_2 = "Eres el peor de todos, te odio."

# Traducimos de forma directa.
textblob_test1 = TextBlob(testing_1).translate(from_lang="es", to="en")
textblob_test2 = TextBlob(testing_2).translate(from_lang="es", to="en")

print("{0} ===> En inglés ===> {1}".format(testing_1,str(textblob_test1)))
print("{0} ===> En inglés ===> {1}".format(testing_2,str(textblob_test2)))

# Revisemos los valores.
print('========== TEXTBLOB ==========')
print('Resultados del string "{0}":\nPolaridad: {1}\n'
      'Subjetividad: {2}'.format(testing_1,textblob_test1.sentiment.polarity,
                                 textblob_test1.sentiment.subjectivity))
print('Resultados del string "{0}":\nPolaridad: {1}\n'
      'Subjetividad: {2}'.format(testing_2,textblob_test2.sentiment.polarity,
                                 textblob_test2.sentiment.subjectivity))


# ¡TextBlob posee muchas otras funcionalidades! Puedes verlas aquí:
# http://textblob.readthedocs.io/en/dev/quickstart.html
