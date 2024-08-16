import random
import names

# List of common dog breeds
BREEDS = [
    "Golden Retriever", "Labrador Retriever", "Poodle", "Bulldog",
    "Beagle", "German Shepherd", "Boxer", "Dachshund", "Rottweiler",
    "Siberian Husky", "Chihuahua", "Shih Tzu", "Doberman", "Great Dane",
    "Yorkshire Terrier", "Cocker Spaniel", "Maltese", "Pit Bull"
]


def generate_random_breed():
    return random.choice(BREEDS)


def generate_random_age():
    return random.randint(1, 15)


def generate_random_name():
    return names.get_first_name()
