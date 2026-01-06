from datetime import datetime, timedelta

class Warranty:
    def __init__(
        self,
        warranty_id: int,
        receipt_id: int,
        duration_months: int,
        expiry_date: str
    ):
        self.id = warranty_id
        self.receipt_id = receipt_id
        self.duration_months = duration_months
        self.expiry_date = expiry_date
# expiry checking logic
    def is_expired(self) -> bool:
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d")
        return datetime.now() > expiry

    def days_remaining(self) -> int:
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d")
        remaining = expiry - datetime.now()
        return max(0, remaining.days)
