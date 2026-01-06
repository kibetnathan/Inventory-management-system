import sqlite3
from pathlib import Path

class DatabaseManager:
    def __init__(self, db_path=None):
        if db_path is None:
            self.db_path = Path(__file__).parent / "tracker.db"
        else:
            self.db_path = Path(db_path)
        self.conn = None
        self.cursor = None

    def connect(self):
            # Connect to SQLite database and create cursor.
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
    

    def create_tables(self):
        # Create tables if they don't exist.
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            store_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            price REAL NOT NULL,
            purchase_date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(store_id) REFERENCES stores(id)
        );
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS warranties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receipt_id INTEGER NOT NULL,
            duration_months INTEGER NOT NULL,
            expiry_date TEXT NOT NULL,
            FOREIGN KEY(receipt_id) REFERENCES receipts(id)
        );
        """)

        self.conn.commit()
    
    def insert_receipt(self, receipt):
        # receipt: Receipt object
        self.cursor.execute("""
            INSERT INTO receipts (user_id, store_id, item_name, price, purchase_date)
            VALUES (?, ?, ?, ?, ?)
        """, (receipt.user_id, receipt.store_id, receipt.item_name, receipt.price, receipt.purchase_date))

        self.conn.commit()
        return self.cursor.lastrowid  # returns the new receipt id
    
    def insert_warranty(self, warranty):
        # warranty: Warranty object
        self.cursor.execute("""
            INSERT INTO warranties (receipt_id, duration_months, expiry_date)
            VALUES (?, ?, ?)
        """, (warranty.receipt_id, warranty.duration_months, warranty.expiry_date))

        self.conn.commit()
        return self.cursor.lastrowid
    
    def fetch_receipts(self):
        # Return all receipts as a list of dicts.
        self.cursor.execute("SELECT * FROM receipts")
        rows = self.cursor.fetchall()
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in rows]
    
    def fetch_expiring_warranties(self, threshold_days=30):
        # Fetch warranties expiring in the next `threshold_days`.
        self.cursor.execute("SELECT * FROM warranties")
        rows = self.cursor.fetchall()

        result = []
        from datetime import datetime, timedelta
        for row in rows:
            expiry_date = datetime.strptime(row[3], "%Y-%m-%d")
            days_remaining = (expiry_date - datetime.now()).days
            if 0 <= days_remaining <= threshold_days:
                result.append(dict(zip([column[0] for column in self.cursor.description], row)))

        return result
    
    def close(self):
        if self.conn:
            self.conn.close()