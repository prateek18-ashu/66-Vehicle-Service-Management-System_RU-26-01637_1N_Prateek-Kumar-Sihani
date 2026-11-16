# 🚗 Vehicle Service Management System

A console-based Python 3 application built for vehicle service centres to manage customer service records, calculate billing with 18% GST, and persist data using file handling.

---

## ✨ Features

* **Complete CRUD Operations:** Add new service tickets, view all active records, update service status (`Pending`, `In Progress`, `Completed`), and delete records.
* **Object-Oriented Architecture:** Uses a `ServiceRecord` class to encapsulate record attributes, billing calculations, and formatted outputs.
* **Fast Record Lookup:** Uses a Python dictionary keyed by vehicle registration number for instant retrieval and updates.
* **Automated GST Calculation:** Automatically applies 18% GST to base service prices.
* **Data Persistence:** Reads from and writes to `services.txt` so records remain saved between runs.

---

## 💰 Service Price List

$$\text{Cost with GST} = \text{Base Price} \times 1.18$$

| Service Type | Base Price | GST (18%) | Total Payable |
| :--- | :---: | :---: | :---: |
| **Oil Change** | Rs. 1500.00 | Rs. 270.00 | **Rs. 1770.00** |
| **Wheel Alignment** | Rs. 800.00 | Rs. 144.00 | **Rs. 944.00** |
| **Full Service** | Rs. 4500.00 | Rs. 810.00 | **Rs. 5310.00** |
| **Brake Repair** | Rs. 2200.00 | Rs. 396.00 | **Rs. 2596.00** |

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Concepts:** OOP, Dictionaries, File I/O (`services.txt`), Input Validation

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/vehicle-service-management-system.git
   cd vehicle-service-management-system
   ```

2. **Run the Python script:**
   *(Replace `main.py` with your actual `.py` filename)*
   ```bash
   python main.py
   ```

---

## 🧪 Test Cases

Starting from an empty `services.txt` file, the application passes the following test scenarios:

| Test Case | Action / Input | Expected Output |
| :--- | :--- | :--- |
| **1. Normal Input** | Add: `MH12AB1234`, `Rohit Patil`, `Car`, `Oil Change` | `Record added. MH12AB1234 \| Oil Change \| Cost incl. 18% GST: Rs. 1770.00 \| Status: Pending` |
| **2. Update Status** | Update `MH12AB1234` $\rightarrow$ `Completed` | `Status updated: Pending -> Completed` |
| **3. Invalid Input (a)** | Add `MH14ZZ0001` with service `Painting` | `Invalid service type. Choose from: Oil Change, Wheel Alignment, Full Service, Brake Repair.` |
| **3. Invalid Input (b)** | Delete `KA01ZZ9999` | `No record found for KA01ZZ9999.` |
| **4. Valid Add & Delete** | Add `CG07XY4321` (`Full Service`), then Delete `CG07XY4321` | `Record added... Rs. 5310.00 \| Status: Pending` $\rightarrow$ `Record for CG07XY4321 deleted.` |

---

## 📄 Documentation
For a detailed breakdown of the architecture and academic problem statement, see [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md).