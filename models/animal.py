class Animal():
    
    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
        
new_animal = Animal(1, "Snickers", "Dog", "Recreation", 1, 4)
