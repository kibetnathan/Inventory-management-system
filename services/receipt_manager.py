from datetime import datetime, timedelta
from models.receipt import Receipt
from models.warranty import Warranty

class ReceiptManager:
    def __init__(self, db_manager):
        """
        db_manager: instance of DatabaseManager
        """
        self.db = db_manager