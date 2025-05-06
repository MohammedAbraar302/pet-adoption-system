import random

# Base Class
class Pet:
    def __init__(self, name, species, age, price):
        self.name = name
        self.species = species
        self.age = age
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Price: {self.price}")

# Derived Classes
class Dog(Pet):
    def __init__(self, name, age, breed, color, price):
        super().__init__(name, "Dog", age, price)
        self.breed = breed
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.color}")

class Cat(Pet):
    def __init__(self, name, age, breed, color, price, eyecolor):
        super().__init__(name, "Cat", age, price)
        self.breed = breed
        self.color = color
        self.eyecolor = eyecolor

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.color}, eyecolor: {self.eyecolor}")

# Pet storage and preferences
pets = {}
preferences = {
    "Dog": ("Bones", "Walk"),
    "Cat": ("Fish", "Nap in sun", "delicate showers")
}

# Add a new pet
def add_pet(pet):
    pet_id = random.randint(1000, 9999)
    while pet_id in pets:
        pet_id = random.randint(1000, 9999)
    pets[pet_id] = pet
    print(f"Pet added with ID: {pet_id}")

# View all pets
def view_pets():
    if not pets:
        print("***NO PETS AVAILABLE......(add pets)***.")
    else:
        for pet_id, pet in pets.items():
            print(f"\nPet ID: {pet_id}")
            pet.display_info()
            print(f"Care Preferences: {preferences[pet.species]}")

# Adopt a pet by ID
def adopt_pet(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        print("Pet adopted successfully!")
    else:
        print("Invalid Pet ID.")

# Menu
def menu():
    while True:
        print("\n--- Pet Adoption System ---")
        print("1. View Pets")
        print("2. Add Pet")
        print("3. Adopt Pet")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_pets()
        elif choice == "2":
            species = input("Enter species (Dog/Cat): ").capitalize()
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            breed = input("Enter breed: ")
            color = input("Enter color: ")
            price = int(input("Enter price: "))
             

            if species == "Dog":
                pet = Dog(name, age, breed, color, price)
            elif species == "Cat":
                pet = Cat(name, age, breed, color, price, eyecolor)
                eyecolor = input("enter eyecolor: ")
            else:
                print("Unsupported species.")
                continue

            add_pet(pet)

        elif choice == "3":
            try:
                pet_id = int(input("Enter Pet ID to adopt: "))
                adopt_pet(pet_id)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run the program
menu()
