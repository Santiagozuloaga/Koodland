meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
            


}
tank=input("Escribe una palabra que no entiendas.")

if tank in meme_dict. keys():
    print(meme_dict[tank])
else:
    print("Esa palabra no existe en el diccionario.")