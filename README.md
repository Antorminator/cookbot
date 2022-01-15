# cookbot
El proyecto "*cookbot*" se ha desarrollado con el objetivo de investigar el uso combinado, como chatbot, del estándar AIML y tecnologías de Inteligencia Artificial.

Para ello, el proyecto se divide en 3 partes:

* Parte 1: chatbot tradicional basado en **AIML**.
* Parte 2: chatbot simple que utiliza **Machine Learning** para procesar el texto introducido por el usuario.
* Parte 3: chatbot que utiliza **Machine Learning** para procesar el texto introducido por el usuario y derivar posteriormente la conversación a un sistema **AIML**.

Se ha utilizado la temática de recetas gastronómicas como concepto común entre los 3 chatbots, para verificar las diferencias de funcionamiento entre uno y otro.
En esta primera versión, los chatbots trabajan con 3 ingredientes distintos y un máximo de 3 categorías de recetas distintas para cada uno:

* Ingrediente "***arroz***", para el cual se pueden elegir las categorías "***entrante***", "***principal***" o "***postre***".
* Ingrediente "***pollo***", para el cual se pueden elegir las categorías "***entrante***" o "***principal***".
* Ingrediente "***pescado***", para el cual se pueden elegir las categorías "***entrante***" o "***principal***".

Adicionalmente, para los chatbots basados en **AIML** existe la posibilidad de **registrar recetas** nuevas y de solicitar un ingrediente-categoría **aleatorios**.

Para la creación, entrenamiento y ejecución del modelo de aprendizaje automático, se ha utilizado la plataforma http://machinelearningforkids.co.uk.

## Ejecución
Para la ejecución del los chatbots basados en AIML, debe de instalarse el framework Python Program-Y (https://github.com/keiffster/program-y):

`%pip install programy`

Ejecución en consola:

`python3 parteX.py # Donde X = nº del chatbot a ejecutar (1, 2 ó 3)`

## Patrones reconocidos por los esquemas AIML
\# QUIERO COCINAR \*

\# ENTRANTE \#

\# PRINCIPAL \#

\# POSTRE \#

\# QUIERO REGISTRAR UNA RECETA NUEVA \#

MUÉSTRAME MIS RECETAS

NO SÉ QUE COCINAR

## Vídeo demostrativo

https://youtu.be/yg7t5GXy4vI
