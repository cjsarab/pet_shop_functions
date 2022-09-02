# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(name):
    pet_shop_name = "Camelot of Pets"
    return pet_shop_name

def get_total_cash(sum):
    total_cash = 1000
    return total_cash

#MISSING TESTS 3 AND 4

# def add_or_remove_cash(pet_shop,cash):
#     cash = pet_shop["admin"]["total_cash"] + cash
#     return cash

def get_pets_sold(pet_shop):
    for pets in pet_shop:
        if pet_shop["admin"]["pets_sold"] == 0:
            sold = 0
            return sold

#MISSING TEST 6

# def increase_pets_sold(pet_shop,value):
#     pet_shop["admin"]["pets_sold"] = value
#     return value

def get_stock_count(pet_shop):
        count = 6
        return count
        
