import sqlite3
import json
from models import Animal

ANIMALS = [
     {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Brixton",
        "species": "Dog",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 3,
        "customerId": 5,
        "status": "Admitted"
    },
    {
        "id": 4,
        "name": "Gypsy",
        "species": "Dog",
        "location": 1,
        "customerId": 2,
        "status": "Admitted"
    }
]

def create_animal(animal):
    
    max_id = ANIMALS[-1]["id"]
    
    new_id = max_id + 1
    
    animal["id"] = new_id
    
    ANIMALS.append(animal)
    
    return animal

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)
        
def update_animal(id, new_animal):
    
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            
            ANIMALS[index] = new_animal
            break


def get_all_animals():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
            
                            """)
        
        animals = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset: 
            
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            
            animals.append(animal.__dict__)
        
    return json.dumps(animals)

#Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exits
    requested_animal = None
    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal
            
    return requested_animal

# print(ANIMALS[1]['id'], ANIMALS[1]['customerId'])
        