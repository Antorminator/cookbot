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

## Ejemplo de conversación
```bash
¿Qué quieres cocinar hoy? # Ejecución del modelo de ML
>Me apetece un buen plato de arroz

Perfecto, vamos a cocinar arroz ! ¿Quieres cocinar un entrante, un principal o un postre? # Clasificación del topic por ML y envío a AIML
>un principal

Tengo las siguientes recetas de platos principales con arroz: 

1- Paella valenciana (no podía faltar!). 
2- Arroz con bogavante. 
3- Risotto de ajo negro con crujiente de parmesano. 
4- Arroz con costillas. 
5- Arroz con presa ibérica al romero. 

Introduce el número del plato para ver su enlace.
>2

https://www.bonviveur.es/recetas/arroz-con-bogavante 
¿Quieres cocinar algo más?
>Quiero registrar una receta nueva # Registro de información directamente con AIML

Perfecto, vamos a registrar una receta nueva. Copia y pega en enlace a continuación.
>Lubina a la sal www.enlace-a.receta

Receta guardada! ;)
>Muéstrame mis recetas    

Lubina a la sal www.enlace-a.receta
>No sé que cocinar # Llamada a suministro aleatorio de recetas

Tengo las siguientes recetas de platos principales de pescado:
                
1- Salmón con salsa de eneldo.

2- Lubina a la donostiarra.

3- Dorada a la sal.

4- Rodaballo a la vizcaína con almejas.

5- Pastel de merluza y gambas.

Introduce el número del plato para ver su enlace
>2

https://www.directoalpaladar.com/recetas-de-pescados-y-mariscos/lubina-a-la-donostiarra-recetas-de-navidad

¿Quieres cocinar algo más?

>No
Que aproveche! 
Hasta pronto! :D
