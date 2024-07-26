import json

from app.data import list_files, open_files



def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if not animal in animals:
        animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animal, file)

        msg = f"Товар '{animal}' успішно додано."
    else:
        msg = f"Товар '{animal}' вже є у списку."

    return msg


def sold_animal(animal: str) -> str:
    animals = open_files.get_animals()
    sold_animals = open_files.get_cured_animals()

    if animal in animals:
        animals.remove(animal)
        animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(sold_animals, file)

        msg = f"Тваринка '{animals}' успішно вилікувана."
    else:
        msg = f"Тваринка '{animals}' відсутня у списку"

    return msg


def remove_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        animals.remove(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Товар '{animal}' успішно видалено"
    else:
        msg = f"Товар '{animal}' відсутній у списку"

    return msg