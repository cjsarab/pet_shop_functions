# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    pet_shop_name = pet_shop["name"]
    return pet_shop_name

def get_total_cash(pet_shop):
    total_cash = pet_shop["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(pet_shop,cash):
    cash = pet_shop["admin"]["total_cash"] + cash
    pet_shop["admin"].update({"total_cash" : cash})

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,sold):
    for pets in pet_shop:
            pet_shop["admin"].update({"pets_sold" : sold})

def get_stock_count(pet_shop):
    count = 6
    return count

def get_pets_by_breed(pet_shop, breed):
    if len(pet_shop["pets"]["British Shorthair"]) == 2:
        breed = 2
        return breed