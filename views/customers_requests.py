CUSTOMERS = [
    {
        "id": 1,
        "name": "Kendrick Lamar",
        "locationId": 3
    },
    {
        "id": 2,
        "name": "Jermaine Cole",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Big Sean",
        "locationId": 2
    }
]

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    
    new_id = max_id + 1
    
    customer["id"] = new_id
    
    CUSTOMERS.append(customer)
    
    return customer

def delete_customer(id):
    customer_index = -1
    
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
            
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)



def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    
    requested_customer = None
    
    for customer in CUSTOMERS:
        
        if customer["id"] == id:
            requested_customer = customer
            
    return requested_customer