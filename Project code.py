import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("athletic_inventory.db")
cursor = conn.cursor()

# Create equipment table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS equipment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    category TEXT,
                    quantity INTEGER,
                    price REAL,
                    usage_instructions TEXT,
                    recommended_sets_reps TEXT,
                    benefits TEXT)''')

conn.commit()


class AthleticInventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Athletic Equipment Inventory")
        self.root.geometry("600x400")
        self.root.configure(bg="#f5f5f5")

        self.main_screen()
    def show_user_inventory(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="User Inventory", font=("Arial", 16, "bold"), bg="#E8F6EF").pack(pady=10)

        tree = ttk.Treeview(self.root, columns=("ID", "Name", "Category", "Quantity", "Price"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Category", text="Category")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")

        cursor.execute("SELECT id, name, category, quantity, price FROM equipment")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

        tree.pack()

        details_frame = tk.Frame(self.root, bg="#E8F6EF")
        details_frame.pack(pady=10)

        details_label = tk.Label(details_frame, text="Select an item to see details", font=("Arial", 12), bg="#E8F6EF")
        details_label.pack()

        def show_details(event):
            selected_item = tree.selection()
            if selected_item:
                item_id = tree.item(selected_item, "values")[0]
                cursor.execute("SELECT usage_instructions, recommended_sets_reps, benefits FROM equipment WHERE id=?", (item_id,))
                result = cursor.fetchone()
                if result:
                    details_label.config(text=f"Usage: {result[0]}\nSets/Reps: {result[1]}\nBenefits: {result[2]}")

        tree.bind("<ButtonRelease-1>", show_details)

        tk.Button(self.root, text="Back", font=("Arial", 12), bg="gray", fg="white", command=self.main_screen).pack(pady=10)
    # --------------------- Main Screen ---------------------
    def main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to Athletic Inventory", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=20)
        tk.Button(self.root, text="Manager", font=("Arial", 14), bg="#FFA07A", command=self.manager_login).pack(pady=10)
        tk.Button(self.root, text="User", font=("Arial", 14), bg="#20B2AA", command=self.show_user_inventory).pack(pady=10)
        tk.Button(self.root, text="Exit", font=("Arial", 14), bg="#FF6347", command=self.root.destroy).pack(pady=10)

    # --------------------- Manager Login ---------------------
    def manager_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Manager Login", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=20)
        tk.Label(self.root, text="Enter Password:", font=("Arial", 12), bg="#f5f5f5").pack()

        password_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
        password_entry.pack(pady=10)

        def check_password():
            if password_entry.get() == "admin123":
                self.manager_screen()
            else:
                messagebox.showerror("Error", "Incorrect Password!")

        tk.Button(self.root, text="Login", font=("Arial", 12), command=check_password, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.main_screen, bg="gray", fg="white").pack(pady=10)

    # --------------------- Manager Dashboard ---------------------
    def manager_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Manager Dashboard", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=20)
        tk.Button(self.root, text="Add Equipment", font=("Arial", 12), command=self.add_equipment, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(self.root, text="View Equipment", font=("Arial", 12), command=self.view_equipment, bg="#008CBA", fg="white").pack(pady=5)
        tk.Button(self.root, text="Update Equipment", font=("Arial", 12), command=self.update_equipment, bg="#FFA500", fg="white").pack(pady=5)
        tk.Button(self.root, text="Delete Equipment", font=("Arial", 12), command=self.delete_equipment, bg="red", fg="white").pack(pady=5)
        tk.Button(self.root, text="Logout", font=("Arial", 12), command=self.main_screen, bg="gray", fg="white").pack(pady=10)

    # --------------------- Add Equipment ---------------------
    def add_equipment(self):
        def save_equipment():
            name = name_entry.get()
            category = category_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()
            usage_instructions = usage_entry.get()
            recommended_sets_reps = sets_reps_entry.get()
            benefits = benefits_entry.get()

            if name and category and quantity and price and usage_instructions and recommended_sets_reps and benefits:
                cursor.execute("INSERT INTO equipment (name, category, quantity, price, usage_instructions, recommended_sets_reps, benefits) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                               (name, category, int(quantity), float(price), usage_instructions, recommended_sets_reps, benefits))
                conn.commit()
                messagebox.showinfo("Success", "Equipment Added!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "All Fields Required!")

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Equipment")
        add_window.geometry("400x400")

        tk.Label(add_window, text="Name").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Category").pack()
        category_entry = tk.Entry(add_window)
        category_entry.pack()

        tk.Label(add_window, text="Quantity").pack()
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack()

        tk.Label(add_window, text="Price").pack()
        price_entry = tk.Entry(add_window)
        price_entry.pack()

        tk.Label(add_window, text="Usage Instructions").pack()
        usage_entry = tk.Entry(add_window)
        usage_entry.pack()

        tk.Label(add_window, text="Recommended Sets/Reps").pack()
        sets_reps_entry = tk.Entry(add_window)
        sets_reps_entry.pack()

        tk.Label(add_window, text="Benefits").pack()
        benefits_entry = tk.Entry(add_window)
        benefits_entry.pack()

        tk.Button(add_window, text="Add", command=save_equipment).pack(pady=5)
    # --------------------- View Equipment ---------------------
    def view_equipment(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Equipment Inventory")
        view_window.geometry("1000x500")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Category", "Quantity", "Price"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Category", text="Category")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        tree.pack(fill="both", expand=True)

        cursor.execute("SELECT id, name, category, quantity, price FROM equipment")
        for record in cursor.fetchall():
            tree.insert("", "end", values=record)

    # --------------------- Update Equipment ---------------------
    def update_equipment(self):
        def save_update():
            equipment_id = id_entry.get()
            name = name_entry.get()
            category = category_entry.get()
            quantity = quantity_entry.get()
            price = price_entry.get()

            cursor.execute("UPDATE equipment SET name=?, category=?, quantity=?, price=? WHERE id=?", 
                           (name, category, int(quantity), float(price), equipment_id))
            conn.commit()
            messagebox.showinfo("Success", "Equipment Updated!")
            update_window.destroy()

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Equipment")
        update_window.geometry("400x400")

        tk.Label(update_window, text="Enter Equipment ID").pack()
        id_entry = tk.Entry(update_window)
        id_entry.pack()

        tk.Label(update_window, text="New Name").pack()
        name_entry = tk.Entry(update_window)
        name_entry.pack()

        tk.Label(update_window, text="New Category").pack()
        category_entry = tk.Entry(update_window)
        category_entry.pack()

        tk.Label(update_window, text="New Quantity").pack()
        quantity_entry = tk.Entry(update_window)
        quantity_entry.pack()

        tk.Label(update_window, text="New Price").pack()
        price_entry = tk.Entry(update_window)
        price_entry.pack()

        tk.Button(update_window, text="Update", command=save_update, bg="#FFA500", fg="white").pack(pady=10)

    # --------------------- Delete Equipment ---------------------
    def delete_equipment(self):
        def confirm_delete():
            cursor.execute("DELETE FROM equipment WHERE id=?", (id_entry.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Equipment Deleted!")
            delete_window.destroy()

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Equipment")
        delete_window.geometry("300x200")

        tk.Label(delete_window, text="Enter Equipment ID").pack()
        id_entry = tk.Entry(delete_window)
        id_entry.pack()
        tk.Button(delete_window, text="Delete", command=confirm_delete, bg="red", fg="white").pack(pady=10)

# Run the Application
root = tk.Tk()
app = AthleticInventoryApp(root)
root.mainloop()
