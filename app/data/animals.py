import json

from app.data import list_files, open_files



def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if not animal in animals:
        animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварина '{animal}' успішно додано."
    else:
        msg = f"Тварина '{animal}' вже є у списку."

    return msg


def cured_animal(animal: str) -> str:
    animals = open_files.get_animals()
    cured_animals = open_files.get_cured_animals()

    if animal in animals:
        animals.remove(animal)
        cured_animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        with open(list_files.cured_animals, "w", encoding="utf-8") as file:
            json.dump(cured_animals, file)

        msg = f"Тваринка '{animal}' успішно вилікувана."
    else:
        msg = f"Тваринка '{animal}' відсутня у списку"

    return msg


def remove_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        animals.remove(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварина '{animal}' успішно видалено"
    else:
        msg = f"Тварина '{animal}' відсутній у списку"

    return msg