from database.db_manager import DatabaseManager
from services.receipt_manager import ReceiptManager
from services.report_generator import ReportGenerator
from utils.validators import validate_receipt_data
from datetime import datetime

# Initialize DatabaseManager
db_manager = DatabaseManager()
db_manager.connect()
db_manager.create_tables()

# Initialize ReceiptManager
receipt_manager = ReceiptManager(db_manager)

# Initialize ReportGenerator
report_generator = ReportGenerator(db_manager, receipt_manager)

def add_purchase_cli():
    try:
        item_name = input("Item name: ")
        price = float(input("Price: "))
        store_id = int(input("Store ID: "))
        purchase_date = input("Purchase date (YYYY-MM-DD): ")
        warranty_months = int(input("Warranty duration (months): "))

        # Validate data
        validate_receipt_data(item_name, price, purchase_date, warranty_months)

        # Add via ReceiptManager
        receipt, warranty = receipt_manager.add_receipt(
            user_id=1,  # assume single user for CLI
            store_id=store_id,
            item_name=item_name,
            price=price,
            purchase_date_str=purchase_date,
            warranty_months=warranty_months
        )

        print(f"Receipt added with ID {receipt.id}, warranty expires {warranty.expiry_date}")

    except Exception as e:
        print(f"Error: {e}")

def view_purchases_cli():
    receipts = db_manager.fetch_receipts()
    if not receipts:
        print("No receipts found.")
        return
    for r in receipts:
        print(f"{r['id']}: {r['item_name']} | Price: {r['price']} | Store ID: {r['store_id']} | Date: {r['purchase_date']}")

def view_expiring_cli():
    threshold = int(input("Show warranties expiring in next how many days? "))
    warranties = receipt_manager.get_expiring_warranties(threshold)
    if not warranties:
        print("No expiring warranties found.")
        return
    for w in warranties:
        print(f"Receipt ID {w['receipt_id']} expires on {w['expiry_date']}")

def import_csv_cli():
    file_path = input("Enter CSV file path: ")
    try:
        report_generator.import_csv(file_path)
        print("CSV imported successfully!")
    except Exception as e:
        print(f"Error importing CSV: {e}")

def export_report_cli():
    file_path = input("Enter output file path (CSV or TXT): ")
    report_type = 'csv' if file_path.endswith('.csv') else 'txt'

    try:
        if report_type == 'csv':
            report_generator.export_warranty_report_csv(file_path)
        else:
            report_generator.export_warranty_report_txt(file_path)
        print(f"Report exported to {file_path}")
    except Exception as e:
        print(f"Error exporting report: {e}")


def main_menu():
    while True:
        print("\n===== Warranty Tracker CLI =====")
        print("1. Add purchase")
        print("2. View all purchases")
        print("3. View expiring warranties")
        print("4. Import from CSV")
        print("5. Export warranty report")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == '1':
            add_purchase_cli()
        elif choice == '2':
            view_purchases_cli()
        elif choice == '3':
            view_expiring_cli()
        elif choice == '4':
            import_csv_cli()
        elif choice == '5':
            export_report_cli()
        elif choice == '6':
            print("Exiting...")
            db_manager.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
