def validate_item_name(name: str):
    if not name.strip():
        raise ValueError("Item name cannot be empty")
    return True

def validate_price(price):
    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number")
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    return True

def validate_warranty_duration(months):
    try:
        months = int(months)
    except ValueError:
        raise ValueError("Warranty duration must be an integer")
    if months <= 0:
        raise ValueError("Warranty duration must be greater than 0")
    return True

from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")
    return True

def validate_receipt_data(item_name, price, purchase_date, warranty_months):
    validate_item_name(item_name)
    validate_price(price)
    validate_date(purchase_date)
    validate_warranty_duration(warranty_months)
    return True