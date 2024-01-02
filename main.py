from pathlib import Path


def save_call_category(interaction_id: str, category: str) -> None:
    pass


def main() -> None:
    call_ids: list[str] = ...  # cargar ids de interacciones (llamadas) a procesar

    for id in call_ids:
        audio_file_path: Path = ...  # descargar audio de la llamada

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
