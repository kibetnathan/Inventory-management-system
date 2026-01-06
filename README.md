# 🧾 Digital Receipt & Warranty Tracker

## 📌 Project Overview

The **Digital Receipt & Warranty Tracker** is a Python-based application that helps users store purchase receipts, manage warranty information, and track warranty expiry dates.
The system uses **Object-Oriented Programming (OOP)** principles, **file handling**, and a **SQLite database backend** to ensure persistent and structured data management.

This project was developed as a **Python capstone project** to demonstrate practical software design, data storage, and file processing skills.

---

## 🎯 Objectives

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