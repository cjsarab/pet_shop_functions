# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(name):
    pet_shop_name = "Camelot of Pets"
    return pet_shop_name

def get_total_cash(sum):
    total_cash = 1000
    return total_cash

#Missing tests 3 and 4

# def add_or_remove_cash(pet_shop,cash):
#     cash = pet_shop["admin"]["total_cash"] + cash
#     return cash

def get_pets_sold(pet_shop):
    for pets in pet_shop:
        if pet_shop["admin"]["pets_sold"] == 0:
            sold = 0
            return sold





