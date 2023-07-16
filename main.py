# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:35:06 2023

@author: Francis
"""

import tkinter as tk

class CafeMenu:
    def __init__(self):
        self.menu_items = {
            "1": {"name": "Burger", "price": 8.99},
            "2": {"name": "Pizza", "price": 10.99},
            "3": {"name": "Pasta", "price": 7.99},
            "4": {"name": "Salad", "price": 5.99},
            "5": {"name": "Soda", "price": 1.99}
        }

    def get_item_price(self, item_id):
        return self.menu_items[item_id]["price"]


class CafeOrder:
    def __init__(self):
        self.order_items = []

    def add_item_to_order(self, item_id, quantity):
        self.order_items.append({"item_id": item_id, "quantity": quantity})

    def calculate_total(self, menu):
        total = 0
        for item in self.order_items:
            price = menu.get_item_price(item["item_id"])
            total += price * item["quantity"]
        return total

    def generate_receipt(self, menu):
        receipt = "Receipt:\n"
        receipt += "--------------------------\n"
        for item in self.order_items:
            item_name = menu.menu_items[item["item_id"]]["name"]
            item_price = menu.get_item_price(item["item_id"])
            item_total = item["quantity"] * item_price
            receipt += f"{item_name} x {item['quantity']} - ${item_total:.2f}\n"
        receipt += "--------------------------\n"
        total = self.calculate_total(menu)
        receipt += f"Total: ${total:.2f}\n"
        receipt += "--------------------------\n"
        return receipt


class CafeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Cafe Management System")
        self.cafe_menu = CafeMenu()
        self.cafe_order = CafeOrder()
        
        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        self.menu_label = tk.Label(self.menu_frame, text="Menu:")
        self.menu_label.pack()

        for key, item in self.cafe_menu.menu_items.items():
            item_label = tk.Label(self.menu_frame, text=f"{key}. {item['name']} - ${item['price']:.2f}")
            item_label.pack()

        self.order_frame = tk.Frame(self.root)
        self.order_frame.pack()

        self.item_id_label = tk.Label(self.order_frame, text="Enter the item ID:")
        self.item_id_label.pack()
        self.item_id_entry = tk.Entry(self.order_frame)
        self.item_id_entry.pack()

        self.quantity_label = tk.Label(self.order_frame, text="Enter the quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.order_frame)
        self.quantity_entry.pack()

        self.add_button = tk.Button(self.order_frame, text="Add to Order", command=self.add_to_order)
        self.add_button.pack()

        self.receipt_text = tk.Text(self.root, height=10, width=50)
        self.receipt_text.pack()

    def add_to_order(self):
        item_id = self.item_id_entry.get()
        quantity = int(self.quantity_entry.get())

        if item_id not in self.cafe_menu.menu_items:
            self.receipt_text.insert(tk.END, "Invalid item ID. Please try again.\n")
        else:
            self.cafe_order.add_item_to_order(item_id, quantity)
            self.receipt_text.delete(1.0, tk.END)
            receipt = self.cafe_order.generate_receipt(self.cafe_menu)
            self.receipt_text.insert(tk.END, receipt)

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeApp(root)
    root.mainloop()