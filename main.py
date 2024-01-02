from pathlib import Path


import requests

def getdata(u, p):
    r = requests.post("https://api.example.com/token", data={"username": u, "password": p})
    if r.status_code == 200:
        return r.json()["token"]
    else:
        return None

def download(id):
    token = getdata("user123", "password456")
    if token:
        res = requests.get(f"https://api.example.com/audio/{id}", headers={"Authorization": f"Bearer {token}"})
        if res.status_code == 200:
            with open(f"{id}.mp3", "wb") as file:
                file.write(res.content)
                return Path(f"{id}.mp3")
            print("Download successful")
        else:
            print("Error downloading file")
    else:
        print("Error getting token")


# Ejemplo para descargar audio con id=12345: download("12345")



def save_call_category(interaction_id: str, category: str) -> None:
    pass


def main() -> None:
    call_ids: list[str] = ...  # cargar ids de interacciones (llamadas) a procesar

    for id in call_ids:
        audio_file_path: Path = download(id)  # descargar audio de la llamada

        transcript: str = ...  # obtener transcripción del audio

        category: str = ...  # obtener categoría de la interacción

        save_call_category(id, category)

    return


if __name__ == '__main__':
    main()



"""
Preguntas:

1. ¿Cómo implementarías los pasos de transcripción y clasificación? ¿Qué técnicas/herramientas/modelos usarías?
2. ¿Se podría hacer el proceso de una forma más eficiente?
3. Si te dijera que ahora cuentas con 5 máquinas diferentes para procesar las llamadas, ¿cómo lo harías?

"""
