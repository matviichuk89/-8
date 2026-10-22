animals = {
    "кіт": "cat",
    "собака": "dog",
    "вовк": "wolf",
    "лисиця": "fox",
    "ведмідь": "bear",
    "заєць": "hare",
    "олень": "deer",
    "тигр": "tiger",
    "лев": "lion",
    "слон": "elephant",
    "мавпа": "monkey",
    "кінь": "horse"
}
english_animals = {}
for ukr, eng in animals.items():
    english_animals[eng] = ukr
print("Початковий словник:")
print(animals)
print("Новий словник:")
print(english_animals)