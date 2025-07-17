meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "WDYM": "Pregunta que es lo que quieres decir",
    "DAMN": "Respuesta que expresa sorpresa o maldición",
    "ROFL": "Respuesta a una broma",
    "SYBAU": "Respuesta que quiere decir que te calles",
    "NPC": "Ser tan malo en un juego como un NPC"
}

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict:
        print(word + ": " + meme_dict[word])
    else:
        print("Esa palabra no está en el diccionario.")
