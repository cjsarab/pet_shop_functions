# WRITE YOUR FUNCTIONS HERE


import numbers
import re


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
    pet_shop["admin"].update({"pets_sold" : sold})

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,breed):
    pets = []
    for pet in pet_shop["pets"]:
        if breed == pet["breed"]:
            pets.append(pet)
    return pets

def find_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if name == pet["name"]:
            return pet

def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, cash):
    cash = customer["cash"] - cash
    customer.update({"cash" : cash})

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    return customer["pets"].append(new_pet)

###OPTIONAL CONTENT

def customer_can_afford_pet(customer,new_pet):
    if new_pet["price"] <= customer["cash"]:
        return True
    else:
        return False
