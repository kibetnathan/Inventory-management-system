from datetime import datetime

class Receipt:
    def __init__(
        self,
        receipt_id: int,
        item_name: str,
        price: float,
        purchase_date: str,
        store_id: int,
        user_id: int
    ):
        self.id = receipt_id
        self.item_name = item_name
        self.price = price
        self.purchase_date = purchase_date
        self.store_id = store_id
        self.user_id = user_id

    #self validation code 
    def validate(self) -> bool:
        if not self.item_name:
            return False

        if self.price <= 0:
            return False

        try:
            datetime.strptime(self.purchase_date, "%Y-%m-%d")
        except ValueError:
            return False

        return True
# dictionary for testing purposes
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "item_name": self.item_name,
            "price": self.price,
            "purchase_date": self.purchase_date,
            "store_id": self.store_id,
            "user_id": self.user_id
        }
