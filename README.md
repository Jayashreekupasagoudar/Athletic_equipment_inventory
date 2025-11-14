# 🏋️‍♂️ Athletic Equipment Inventory System  
*A Python + Tkinter + SQLite Inventory Management Application*

---

## 📌 Project Overview

The **Athletic Equipment Inventory System** is a GUI-based Python application designed to manage equipment in **gyms, sports centers, and fitness clubs**. The system provides **role-based access**, allowing:

- **Managers** to add, update, delete, and view inventory data.
- **Users** to browse equipment and view usage instructions, recommended sets/reps, and benefits.

Technologies used:
- Python  
- Tkinter (GUI)  
- SQLite3 (Database)  

---

## 🎯 Features

### 🔐 Role-Based Login
- **Manager Login**
  - Password protected (`admin123`)
  - Full access to inventory operations
- **User View**
  - Browse all equipment
  - View detailed usage information

### 📦 Inventory Management (Manager)
- Add new equipment
- Update existing equipment
- Delete equipment
- View all equipment in a table (TreeView)

### 🧑‍💻 User Functionalities
- View equipment list
- View usage instructions
- Recommended workout sets & reps
- Benefits of each equipment

### 🗄️ Database (SQLite3)
- Secure and structured storage
- Preloaded equipment data
- Ensures data integrity

---

## 🏗️ Project Structure
---

## ⚙️ How It Works

### 1️⃣ Startup Screen
User selects:
- Manager  
- User  
- Exit  

### 2️⃣ Manager Dashboard
After entering the correct password:
- Add, Update, Delete equipment  
- View inventory  

### 3️⃣ User Dashboard
Users can:
- View all equipment  
- Click an item to view detailed instructions & benefits  

### 4️⃣ Database Fields
- Equipment ID  
- Name  
- Category  
- Quantity  
- Price  
- Usage Instructions  
- Sets/Reps  
- Benefits  

---

## 🧩 Modules Overview

### ✔ Database Module
Creates and manages SQLite tables.

### ✔ CRUD Module
Handles add, update, delete, and view operations.

### ✔ GUI Module
Menu-driven Tkinter interface using:
- Frames  
- Buttons  
- Entry fields  
- TreeView  

### ✔ Validation & Error Handling
Prevents invalid inputs and missing IDs.

---

## 🚀 How to Run

### 1. Check Python Installation
```bash
python --version
python "Project code.py"



## 📸 Screenshots
(Add screenshots of your application here)


## 🔮 Future Enhancements
- Add search and filter options
- Generate Excel/CSV reports
- Create a web version using Flask + React
- Add maintenance reminders for equipment
- Add user login & profile system

## 🏁 Conclusion
This project provides a complete and efficient solution for managing athletic equipment. 
With a role-based system, GUI interface, and SQLite database, it ensures accuracy, ease of use, 
and scalability for gyms, sports centers, and training facilities.





