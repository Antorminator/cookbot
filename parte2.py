import requests

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
    
    #print("Entrenando text: ",text," - label: ",label)
    print("Ah, vale! Perfecto, déjame unos instantes que lo anote para la próxima vez...")

    # Integración del nuevo término en la clase correspondiente del modelo
    url = urlML4K + key + "/train"

    response = requests.post(url, json={ "data" : text, "label" : label })

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
    question = input("> ")
    answer = classify(question)
    
    answerclass = answer['class_name']
    confidence=answer['confidence']
    
    if confidence<75: # Si el nivel de confianza en la predicción es menor al 75%, re-pregunta al usuario para entrenar el modelo
        print('Disculpa, no te he entendido. ¿Quieres cocinar arroz, pollo o pescado?')
        answerclass=answer_question();
        store_training(question, answerclass)

    return answerclass # Retorno el valor de clasificación obtenido
    

def get_recipes(answerclass):

    print('Tengo las siguientes recetas:')

    if answerclass=='entrantes_arroz':
        
        print('-Sushi: https://www.directoalpaladar.com/recetario/27-recetas-sushi-para-celebrar-dia-mundial-sushi-al-gusto-todos')
        print('-Ensalada de arroz: https://www.petitchef.es/recetas/entrante/ensalada-de-arroz-facil-y-rapida-fid-1570733/')
        print('-Saquitos crujientes de arroz con marisco: https://sevilla.abc.es/gurme/recetas/saquitos-crujientes-de-arroz-con-marisco')
        print('-Tartaletas con arroz y gambas: https://www.lecturas.com/recetas/tartaletas-arroz-y-gambas_6410.html')
        print('-Flanes de arroz, cebolla y beicon: https://www.divinacocina.es/flanes-de-arroz-cebolla-y-bacon/')

    elif answerclass=='principales_arroz':

        print('-Paella valenciana (no podía faltar!): https://www.directoalpaladar.com/recetas-de-arroces/paella-valenciana-receta-tradicional')
        print('-Arroz con bogavante: https://www.bonviveur.es/recetas/arroz-con-bogavante')
        print('-Risotto de ajo negro con crujiente de parmesano: https://www.directoalpaladar.com/recetas-de-arroces/risotto-de-ajo-negro-con-crujiente-de-parmesano-receta-para-enamorar')
        print('-Arroz con costillas: https://www.pequerecetas.com/receta/arroz-con-costillas/')
        print('-Arroz con presa ibérica al romero: https://gastronomiaycia.republica.com/2020/05/12/arroz-con-presa-de-cerdo-iberico-al-romero-tu-receta-de-arroz-para-el-proximo-domingo/')

    elif answerclass=='postres_arroz':

        print('-Arroz con leche: https://www.recetasdeescandalo.com/como-hacer-arroz-con-leche-receta-de-postre-casero-tradicional/')
        print('-Arroz perfumado con cardamomo y rosas: https://gastronomiaycia.republica.com/2012/10/02/arroz-perfumado-con-cardamomo-y-rosas/')
        print('-Pastel de arroz, chocolate y nueces: https://gastronomiaycia.republica.com/2013/03/17/pastel-de-arroz-chocolate-y-nueces/')
        print('-Arroz dulce al horno: https://www.rebanando.com/receta-46840-arroz-al-horno-dulce-o-pastel-de-arroz-con-leche.htm')
        print('-Arroz jazmín con mango: https://mahatmarice.com/es/recetas/arroz-con-mango/')

    elif answerclass=='entrantes_pollo':
        
        print('-Nuggets de pollo caseros: https://www.directoalpaladar.com/recetas-de-aperitivos/como-hacer-nuggets-caseros-receta-con-thermomix')
        print('-Gyozas de pollo, zanahoria y champiñones: https://www.petitchef.es/recetas/entrante/gyozas-de-pollo-zanahoria-y-champinones-fid-1575328')
        print('-Ensalada césar con pollo: https://www.recetasderechupete.com/receta-de-ensalada-cesar/681/')
        print('-Brochetas de pollo al estilo Satay: https://www.directoalpaladar.com/tapas-y-pinchos/brochetas-de-pollo-estilo-satay-receta-para-el-picoteo')
        print('-Paté de pollo al oporto: http://www.nomecomesnada.es/pate-al-oporto/')
        
    elif answerclass=='principales_pollo':

        print('-Pollo a la naranja: https://www.cocinacaserayfacil.net/pollo-ala-naranja/')
        print('-Pollo teriyaki: https://www.recetasderechupete.com/como-preparar-pollo-teriyaki-de-manera-facil-y-rapida/9848/')
        print('-Albóndigas de pollo: https://www.cocinacaserayfacil.net/albondigas-de-pollo-en-salsa-de-cebolla/')
        print('-Pollo con mostaza y cebolla caramelizada: https://www.directoalpaladar.com/recetas-de-carnes-y-aves/receta-pollo-salsa-cremosa-mostaza-champinones-cebolla-caramelizada-para-mojar-pan-disfrutar-tupper')
        print('-Pollo tikka masala: https://www.directoalpaladar.com/recetas-de-carnes-y-aves/pollo-tikka-masala-receta-pollo-especiado-popular-mundo')
        
    elif answerclass=='entrantes_pescado':
        
        print('-Salmón marinado: https://www.pequerecetas.com/receta/salmon-marinado/')
        print('-Bombones de atún con mayonesa: https://www.juliaysusrecetas.com/2016/08/bombones-de-atun-con-mayonesa.html')
        print('-Brandada de bacalao: https://www.hogarmania.com/cocina/recetas/pescados-mariscos/brandada-bacalao-42089.html')
        print('-Almejas a la marinera: https://elmundoenrecetas.com/receta/almejas-a-la-marinera')
        print('-Vieiras con tomate, hierbabuena y lima: https://www.directoalpaladar.com/recetas-de-pescados-y-mariscos/vieiras-a-la-plancha-con-agua-de-tomate-a-la-hierbabuena-y-lima-receta-ligera')

    elif answerclass=='principales_pescado':
        
        print('-Salmón con salsa de eneldo: https://www.divinacocina.es/salmon-con-salsa-de-eneldo/')
        print('-Lubina a la donostiarra: https://www.directoalpaladar.com/recetas-de-pescados-y-mariscos/lubina-a-la-donostiarra-recetas-de-navidad')
        print('-Dorada a la sal: https://www.recetasderechupete.com/dorada-a-la-sal-y-al-horno-receta-paso-a-paso/11648/')
        print('-Rodaballo a la vizcaína con almejas: https://www.lecturas.com/recetas/rodaballo-almejas-a-vizcaina_8839.html')
        print('-Pastel de merluza y gambas: https://www.bonviveur.es/recetas/pastel-de-merluza-y-gambas')


# Inicio del chatbot

print('¿Qué quieres cocinar hoy?')

while True:
    answerclass=answer_question()
    get_recipes(answerclass)
    print('¿Qué más quieres cocinar?')