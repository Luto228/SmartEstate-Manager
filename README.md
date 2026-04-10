## Apartment Management System ##

A lightweight Python module for managing real estate data. This project demonstrates the use of @property decorators for data validation and protecting attributes from incorrect modifications.

## 📋 Features
The current version of the Apartament class supports:

Price Validation: Ensures the price is set to 1000 units or higher.

Area Control: Prevents the entry of negative or zero square meters.

Smart Address Handling: * Automatically removes spaces from the address string.

Enforces a minimum length of at least 10 characters.

One-time Write: The address can only be set once during initialization (controlled via the CanWrite flag).

## 🛠 Usage
Example of how to create and use an instance:

Python
# Creating an apartment instance
p = Apartament('TheBestHouse', 60, 1001)

print(p.addres)
print(p.area)
print(p.price) 

## ⚠️ Error Handling
The class raises a **ValueError** in the following cases:

**Price Validation**: The price is set to less than 1000.

**Area Validation**: The area is less than or equal to 0.

**Address Constraints**: The address is shorter than 10 characters or you attempt to modify it after it has been already set.

**Purchase Logic**: You try to buy an apartment that is already sold or if you have insufficient funds.

## 🚀 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone this repository (or download `Main.py`).
3. Run the script:
   ```bash
   python Main.py
   ```