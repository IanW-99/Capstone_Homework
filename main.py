from dataclasses import dataclass


def calculate_charge(state: str, cart: list):
    if check_state(state):
        total = 0

        for item in cart:
            total += abs(item.unit_price)
            total += get_item_tax(state, item.item_type, abs(item.unit_price))
        return round(total, 2)

    else:
        raise ValueError()


def check_state(state: str):
    if state == "Massachusetts" or state == "Maine" or state == "New Hampshire":
        return True
    else:
        return False


def get_item_tax(state: str, item_type: str, unit_price: float):
    if state == "Massachusetts":
        item_tax = get_mass_tax(item_type, unit_price)
    elif state == "Maine":
        item_tax = get_maine_tax(item_type, unit_price)
    else:
        item_tax = 0

    return item_tax


def get_mass_tax(item_type: str, unit_price: float):
    if item_type == "Wic Eligible food":
        item_tax = unit_price * 0.0625
    elif item_type == "Clothing":
        if unit_price <= 175.00:
            item_tax = 0
        else:
            item_tax = (unit_price - 175) * 0.0625
    else:
        item_tax = unit_price * 0.0625

    return item_tax


def get_maine_tax(item_type: str, unit_price: float):
    if item_type == "Wic Eligible food":
        item_tax = 0
    elif item_type == "Clothing":
        item_tax = unit_price * 0.055
    else:
        item_tax = unit_price * 0.055

    return item_tax


@dataclass
class CartItem:
    item_name: str
    unit_price: float
    item_type: str
