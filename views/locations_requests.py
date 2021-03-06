LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville Kennels",
        "address": "100 Succeeding lane"
    },
    {
        "id": 2,
        "name": "Boro Kennels",
        "address": "100 Succeeding lane"
    },
    {
        "id": 3,
        "name": "Chattanooga Kennels",
        "address": "100 Succeeding lane"
    }
]

def create_location(location):
    
    max_id = LOCATIONS[-1]["id"]
    
    new_id = max_id + 1
    
    location["id"] = new_id
    
    LOCATIONS.append(location)
    
    return location

def delete_location(id):
    
    location_index = -1
    
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            
            location_index = index
            
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            
            LOCATIONS[index] = new_location
            break
    
    

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
            
    return requested_location