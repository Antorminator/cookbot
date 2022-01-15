import requests
from programy.clients.embed.datafile import EmbeddedDataFileBot

key = "CHANGE FOR YOUR ML4K API KEY"
urlML4K = "https://machinelearningforkids.co.uk/api/scratch/"

# Esta función pasará el texto introducido por el usuario al modelo de
# de ML4K y devolverá la clasificación con mayor porcentaje de coincidencia
def classify(text):
    url = urlML4K + key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        response_data = response.json()
        top_match = response_data[0]
        return top_match
    else:
        response.raise_for_status()

# Esta función sirve para entrenar el modelo de aprendizaje automático con nuevas frases
def store_training(text, label):
    
    # Integración del nuevo término en la clase correspondiente del modelo
    url = urlML4K + key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })
    
    #print("Entrenando text: ",text," - label: ",label)
    print("Ah, vale! Perfecto, déjame unos instantes que lo anote para la próxima vez...")

    if response.ok == False:
        # if something went wrong, display the error
        print (response.json())

    # Entrenamiento del modelo
    url = urlML4K + key + "/models"

    response = requests.post(url)

    if response.ok == False:
        # if something went wrong, display the error
        print (response.json())

# Esta función recibe el texto introducido por el usuario, lo clasifica y devuelve la respuesta correspondiente
def answer_question():
    question=input(">")
    
    answer=classify(question)
    res=answer['class_name']

    confidence=answer['confidence']
    
    #print('Confianza: ',confidence)

    if confidence < 70:
        print('Perdona, no te he entendido. ¿Quieres cocinar pollo, arroz o pescado?')
        res=answer_question();
        store_training(question, res)

    return res
    

# Pregunta cuya respuesta será procesada por el modelo de ML4K
print('¿Qué quieres cocinar hoy?')

topic = answer_question() 

# Carga del AIML del chatbot y envío de la clasificación obtenida
chatbot = EmbeddedDataFileBot(files={'aiml':['archivos_aiml_parte3']}, defaults={})

print(chatbot.ask_question(topic))

# Continuación del procesamiento con AIML
try:
    answer=''

    while answer!='Que aproveche! Hasta pronto! :D.': # La condición de salida del programa es el mensaje de despedida del chatbot (AIML)
        
        answer=chatbot.ask_question(input('>')) # Llamada al chatbot AIML

        # Con el siguiente if compruebo respuestas clave del chatbot AIML
        # Condición 1 = se reinicia la conversación, por lo que igual que se hace al principio, se llama al modelo de ML
        # Condición 2: AIML no ha entendido la respuesta, por lo que se llama al modelo de ML para intentar averiguar el topic
        if answer == '¿Qué otra cosa quieres cocinar?' or answer=='None': 
        
            answer=answer.replace('None','Mmm, no te he entendido. ¿Qué otra cosa quieres cocinar?') # Para no devolver "None"
            print(answer)
            
            topic=answer_question() # Nueva llamada al modelo de ML
            answer=chatbot.ask_question(topic) # Envío del topic obtenido a AIML
            
        print(answer)

except:
    pass