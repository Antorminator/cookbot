from programy.clients.embed.datafile import EmbeddedDataFileBot

chatbot = EmbeddedDataFileBot(files={'aiml':['archivos_aiml_parte1']}, defaults={}) # Carga de los archivos AIML que contienen las reclas del bot

try:
    while True:
        
        answer = chatbot.ask_question(input('>')) # Lanzamiento del chatbot AIML con lo que introduzca el usuario
        
        if answer!='None':
            print(answer)
        else:
            print('Disculpa, no te he entendido, ¿quieres cocinar arroz, pollo o pescado?')
except:
    pass