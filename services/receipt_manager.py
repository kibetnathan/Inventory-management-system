from datetime import datetime, timedelta
from models.receipt import Receipt
from models.warranty import Warranty

class ReceiptManager:
    def __init__(self, db_manager):

        # db_manager: instance of DatabaseManager

        self.db = db_manager

    def add_receipt(self, user_id, store_id, item_name, price, purchase_date_str, warranty_months):

        # Creates Receipt + Warranty and saves them via DatabaseManager

        # Validate & parse date
        try:
            purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("purchase_date must be YYYY-MM-DD")

        # Create Receipt object
        receipt = Receipt(
            receipt_id=None,  # DB will generate ID
            user_id=user_id,
            store_id=store_id,
            item_name=item_name,
            price=price,
            purchase_date=purchase_date_str
        )

        # Save receipt via DB
        receipt_id = self.db.insert_receipt(receipt)
        receipt.id = receipt_id

        # Calculate warranty expiry
        expiry_date = purchase_date + timedelta(days=warranty_months*30)  # Approximate 30 days per month
        expiry_date_str = expiry_date.strftime("%Y-%m-%d")

        # Create Warranty object
        warranty = Warranty(
            warranty_id=None,
            receipt_id=receipt.id,
            duration_months=warranty_months,
            expiry_date=expiry_date_str
        )

        # Save warranty via DB
        warranty_id = self.db.insert_warranty(warranty)
        warranty.id = warranty_id

        # Return created objects
        return receipt, warranty
    
    def get_expiring_warranties(self, threshold_days=30):
        return self.db.fetch_expiring_warranties(threshold_days)