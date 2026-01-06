import csv
from datetime import datetime, timedelta
from models.receipt import Receipt
from models.warranty import Warranty
from services.receipt_manager import ReceiptManager

class ReportGenerator:
    def __init__(self, db_manager, receipt_manager):
        self.db = db_manager
        self.rm = receipt_manager

    def import_csv(self, file_path):

        # Reads CSV and saves receipts + warranties to DB

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Extract columns
                item_name = row['item_name']
                price = float(row['price'])
                store_name = row['store']
                purchase_date = row['purchase_date']
                warranty_months = int(row['warranty_months'])

                #  Save store if not exists (simplified)
                self.db.cursor.execute("SELECT id FROM stores WHERE name = ?", (store_name,))
                store = self.db.cursor.fetchone()
                if store:
                    store_id = store[0]
                else:
                    self.db.cursor.execute("INSERT INTO stores (name) VALUES (?)", (store_name,))
                    self.db.conn.commit()
                    store_id = self.db.cursor.lastrowid

                #  Use ReceiptManager to create receipt + warranty
                # Assuming user_id = 1 for CSV imports
                self.rm.add_receipt(
                    user_id=1,
                    store_id=store_id,
                    item_name=item_name,
                    price=price,
                    purchase_date_str=purchase_date,
                    warranty_months=warranty_months
                )
    def export_warranty_report_csv(self, file_path, threshold_days=None):

        # Exports all warranties or expiring warranties to CSV

        if threshold_days:
            warranties = self.rm.get_expiring_warranties(threshold_days)
        else:
            warranties = self.db.fetch_expiring_warranties(365*100)  # All warranties

        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['item_name', 'store', 'expiry_date', 'days_remaining']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for w in warranties:
                expiry_date = datetime.strptime(w['expiry_date'], "%Y-%m-%d")
                days_remaining = max(0, (expiry_date - datetime.now()).days)
                # Fetch item name + store from receipts
                self.db.cursor.execute("SELECT item_name, store_id FROM receipts WHERE id = ?", (w['receipt_id'],))
                r = self.db.cursor.fetchone()
                item_name = r[0]
                store_id = r[1]
                self.db.cursor.execute("SELECT name FROM stores WHERE id = ?", (store_id,))
                store = self.db.cursor.fetchone()[0]

                writer.writerow({
                    'item_name': item_name,
                    'store': store,
                    'expiry_date': w['expiry_date'],
                    'days_remaining': days_remaining
                })
                
    def export_warranty_report_txt(self, file_path, threshold_days=None):
        warranties = self.rm.get_expiring_warranties(threshold_days)
        with open(file_path, 'w', encoding='utf-8') as f:
            for w in warranties:
                expiry_date = datetime.strptime(w['expiry_date'], "%Y-%m-%d")
                days_remaining = max(0, (expiry_date - datetime.now()).days)
                # Fetch receipt + store
                self.db.cursor.execute("SELECT item_name, store_id FROM receipts WHERE id = ?", (w['receipt_id'],))
                r = self.db.cursor.fetchone()
                item_name = r[0]
                store_id = r[1]
                self.db.cursor.execute("SELECT name FROM stores WHERE id = ?", (store_id,))
                store = self.db.cursor.fetchone()[0]

                f.write(f"{item_name} | {store} | {w['expiry_date']} | {days_remaining} days remaining\n")