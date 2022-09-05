# WRITE YOUR FUNCTIONS HERE

#Locates and returns pet shop name
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#Locates and returns pet shop's total cash
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#Updates dictionary with new cash value
def add_or_remove_cash(pet_shop,cash):
    cash = pet_shop["admin"]["total_cash"] + cash
    pet_shop["admin"].update({"total_cash" : cash})

#Locates and returns the value of [pets sold]
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#Updates dictionary with new pets sold value
def increase_pets_sold(pet_shop,sold):
    pet_shop["admin"].update({"pets_sold" : sold})

#Returns count of pet list
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#Creates a new list [pets] and populates it with returned breeds
def get_pets_by_breed(pet_shop,breed):
    pets = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            pets.append(pet)
    return pets

#Locates and returns pet by name
def find_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            return pet

#Locates and removes pet by name
def remove_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            pet_shop["pets"].remove(pet)
            return

#Adds new pet to list of pets
def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

#Locates and returns customer cash
def get_customer_cash(customers):
    return customers["cash"]

#Removes customers cash
def remove_customer_cash(customer, cash):
    cash = customer["cash"] - cash
    customer.update({"cash" : cash})

#Locates, counts and returns number of pets in customer's inventory
def get_customer_pet_count(customer):
    return len(customer["pets"])

#Adds pet to customer list
def add_pet_to_customer(customer,new_pet):
    return customer["pets"].append(new_pet)

###OPTIONAL CONTENT

def customer_can_afford_pet(customer,new_pet):
    if new_pet["price"] <= customer["cash"]:
        return True
    else:
        return False

#INTEGRATION TESTS

def sell_pet_to_customer(pet_shop,pet,customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop,pet["name"])
        add_pet_to_customer(customer,pet)
        remove_customer_cash(customer,pet["price"])
        add_or_remove_cash(pet_shop,pet["price"])
        increase_pets_sold(pet_shop,1)




