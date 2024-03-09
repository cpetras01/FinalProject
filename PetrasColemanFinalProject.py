import tkinter as tk
from tkinter import messagebox

class RestaurantApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurant Management System")
        self.master.geometry("400x300")

        self.order = []  # List to store the ordered items

        self.create_main_window()

    def create_main_window(self): # This creates the main window with the buttons for the staff to click
        self.main_window = tk.Frame(self.master)
        self.main_window.pack()

        drinks_button = tk.Button(self.main_window, text="Order Drinks", command=self.open_drinks_window)
        drinks_button.pack(pady=20)

        appetizers_button = tk.Button(self.main_window, text="Order Appetizers", command=self.open_appetizers_window)
        appetizers_button.pack(pady=20)

        main_meals_button = tk.Button(self.main_window, text="Order Main Meals", command=self.open_main_meals_window)
        main_meals_button.pack(pady=20)

        desserts_button = tk.Button(self.main_window, text="Order Desserts", command=self.open_desserts_window)
        desserts_button.pack(pady=20)

        exit_button = tk.Button(self.main_window, text="Exit", command=self.master.destroy)
        exit_button.pack(pady=20)

        self.total_order_label = tk.Label(self.master, text="Total Order:")
        self.total_order_label.pack(pady=20)

        self.update_total_order_label() # This updates the list once all orders have been entered

    def open_drinks_window(self): # Opens drink window
        self.drinks_window = tk.Toplevel(self.master)
        self.drinks_window.title("Order Drinks")
        self.drinks_window.geometry("400x200")

        label = tk.Label(self.drinks_window, text="Enter your drink order:")
        label.pack(pady=10)

        self.drink_entry = tk.Entry(self.drinks_window, width=30)
        self.drink_entry.pack(pady=10)

        completed_button = tk.Button(self.drinks_window, text="Completed", command=self.close_drinks_window)
        completed_button.pack(pady=10)

    def close_drinks_window(self): # Closes drink window
        drink_order = self.drink_entry.get()
        self.order.append(f"Drink: {drink_order}")
        self.drinks_window.destroy()
        self.update_total_order_label()

    def open_appetizers_window(self): #Opens appetizer window
        self.appetizers_window = tk.Toplevel(self.master)
        self.appetizers_window.title("Order Appetizers")
        self.appetizers_window.geometry("400x200")

        label = tk.Label(self.appetizers_window, text="Enter your appetizer order:")
        label.pack(pady=10)

        self.appetizer_entry = tk.Entry(self.appetizers_window, width=30)
        self.appetizer_entry.pack(pady=10)

        completed_button = tk.Button(self.appetizers_window, text="Completed", command=self.close_appetizers_window)
        completed_button.pack(pady=10)

    def close_appetizers_window(self): #Closes appetizer window
        appetizer_order = self.appetizer_entry.get()
        self.order.append(f"Appetizer: {appetizer_order}")
        self.appetizers_window.destroy()
        self.update_total_order_label()

    def open_main_meals_window(self): # Opens main meals window
        self.main_meals_window = tk.Toplevel(self.master)
        self.main_meals_window.title("Order Main Meals")
        self.main_meals_window.geometry("400x200")

        label = tk.Label(self.main_meals_window, text="Enter your main meal order:")
        label.pack(pady=10)

        self.main_meal_entry = tk.Entry(self.main_meals_window, width=30)
        self.main_meal_entry.pack(pady=10)

        completed_button = tk.Button(self.main_meals_window, text="Completed", command=self.close_main_meals_window)
        completed_button.pack(pady=10)

    def close_main_meals_window(self): # Closes main meal window
        main_meal_order = self.main_meal_entry.get()
        self.order.append(f"Main Meal: {main_meal_order}")
        self.main_meals_window.destroy()
        self.update_total_order_label()

    def open_desserts_window(self): #Opens dessert window
        self.desserts_window = tk.Toplevel(self.master)
        self.desserts_window.title("Order Desserts")
        self.desserts_window.geometry("400x200")

        label = tk.Label(self.desserts_window, text="Enter your dessert order:")
        label.pack(pady=10)

        self.dessert_entry = tk.Entry(self.desserts_window, width=30)
        self.dessert_entry.pack(pady=10)

        completed_button = tk.Button(self.desserts_window, text="Completed", command=self.close_desserts_window)
        completed_button.pack(pady=10)

    def close_desserts_window(self): # Closes Dessert window
        dessert_order = self.dessert_entry.get()
        self.order.append(f"Dessert: {dessert_order}")
        self.desserts_window.destroy()
        self.update_total_order_label()

    def update_total_order_label(self):
        self.total_order_label.config(text="Total Order:\n" + "\n".join(self.order))


def main(): #Opens application
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
