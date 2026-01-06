# Digital Receipt & Warranty Tracker

## Project Overview

The **Digital Receipt & Warranty Tracker** is a Python-based application that helps users store purchase receipts, manage warranty information, and track warranty expiry dates.
The system uses **Object-Oriented Programming (OOP)** principles, **file handling**, and a **SQLite database backend** to ensure persistent and structured data management.

This project was developed as a **Python capstone project** to demonstrate practical software design, data storage, and file processing skills.

---

## Objectives

* Store purchase and receipt information digitally
* Track warranty durations and expiry dates
* Identify warranties that are about to expire
* Demonstrate the use of Python, OOP, file handling, and databases
* Build a modular and well-structured application

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Database:** SQLite
* **Paradigm:** Object-Oriented Programming (OOP)
* **Interface:** Command Line Interface (CLI)
* **File Handling:** CSV and TXT file processing

---

## 📂 Project Structure
```text
warranty_tracker/
 ├── main.py
 ├── models/
 │   ├── user.py
 │   ├── receipt.py
 │   ├── warranty.py
 │   └── store.py
 ├── database/
 │   └── db_manager.py
 ├── services/
 │   ├── receipt_manager.py
 │   └── report_generator.py
 ├── files/
 │   ├── import_purchases.csv
 │   └── warranty_report.txt
 └── utils/
     └── validators.py
```

---

## System Design

### Object-Oriented Design

The system is divided into multiple classes, each with a specific responsibility:

* **User** – Represents a system user
* **Store** – Represents a store where an item was purchased
* **Receipt** – Stores purchase details such as item name, price, and date
* **Warranty** – Handles warranty duration, expiry date, and status
* **DatabaseManager** – Manages all database operations
* **ReceiptManager** – Handles business logic and validation
* **ReportGenerator** – Manages file import and export operations

This separation ensures **maintainability**, **readability**, and **scalability**.

---

## Database Design

The application uses **SQLite** for data persistence.

### Tables:

* `users`
* `stores`
* `receipts`
* `warranties`

Each table is related using primary and foreign keys to maintain data integrity.

---

## 📁 File Handling

The system supports file operations to meet the file handling requirement:

### Import

* Purchases can be imported from a **CSV file**
* Each row is processed and stored in the database

### Export

* Warranty reports are exported to a **TXT or CSV file**
* Reports include:
  * Item name
  * Store
  * Expiry date
  * Days remaining

---

## ⚙️ How to Run the Project

1. Ensure Python is installed on your system
2. Clone or download the project folder
3. Navigate to the project directory
4. Run the application:
```bash
python main.py
```

---

## Application Features

* Add new purchase records
* Assign and calculate warranty expiry dates
* View all stored receipts
* View warranties that are nearing expiry
* Import purchase data from a CSV file
* Export warranty reports to a file

---

## Limitations

* The application uses a CLI instead of a graphical interface
* No user authentication is implemented
* Warranty notifications are simulated via reports only

---

## Future Improvements

* Add a graphical user interface (GUI)
* Implement user authentication
* Email or SMS notifications for expiring warranties
* Support for receipt image uploads

---

## Conclusion

This project successfully demonstrates the use of **Python**, **Object-Oriented Programming**, **file handling**, and **database management** in building a practical, real-world application.
The modular design ensures the system is easy to extend and maintain.