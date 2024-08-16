import tkinter as tk
from tkinter import ttk
import random

# Create the main window
root = tk.Tk()
root.title("Student info")
root.geometry("1000x500")

label1 = tk.Label(root, text="Name")
label1.pack(pady=(10, 0))
text_widget3 = tk.Text(root, height=5, width=40)
text_widget3.pack(pady=10)

label1 = tk.Label(root, text="Age")
label1.pack(pady=(10, 0))
text_widget1 = tk.Text(root, height=5, width=40)
text_widget1.pack(pady=10)

label1 = tk.Label(root, text="Occupation")
label1.pack(pady=(10, 0))
text_widget2 = tk.Text(root, height=5, width=40)
text_widget2.pack(pady=10)

def change_row_color(): 
    # Define a list of possible colors
    colors = ["lightblue", "lightgreen", "lightpink", "lightyellow", "lightgrey"]
    # Select a random color from the list
    random_color = random.choice(colors)
    # Return the selected color
    return random_color

def submit_data():
    # Get input from text widgets
    age= text_widget1.get("1.0", tk.END).strip()  # Get all text from the Text widget
    name = text_widget3.get("1.0", tk.END).strip()
    occupation = text_widget2.get("1.0", tk.END).strip()

    # Create a dictionary with the input data
    dataf = {"Name": name, "Age": age, "Occupation": occupation}
    bg_color = change_row_color()
    # Insert the data into the Treeview
    for key, value in dataf.items():
        # Change row color randomly
        
        # Insert into the Treeview with the random background color
        tree.insert("", "end", values=(key, value), tags=(bg_color,))
        tree.tag_configure(bg_color, background=bg_color)

# Button to submit data
submit_button = ttk.Button(root, text="Submit", command=submit_data)
submit_button.pack(pady=10)

# Sample data
data1 = {"Name": "Alice", "Age": 25, "Occupation": "Engineer"}
data2 = {"Name": "Rey", "Age": 5, "Occupation": "Computer Engineer"}
data3 = {"Name": "Rambo Gama", "Age": 95, "Occupation": "Web Developer"}
data4 = {"Name": "Janta Brown", "Age": 11, "Occupation": "Accountant"}
info = [data1, data2, data3, data4]

# Creating a Treeview widget
tree = ttk.Treeview(root, columns=("Key", "Value"), show='headings')

# Style configurations
style = ttk.Style()
style.configure("Treeview", 
                font=("Helvetica", 12), 
                foreground="black", 
                background="white", 
                rowheight=30,  # Increased row height for better visual distinction
                highlightthickness=1,  # Thickness for highlighting (border)
                relief="solid")  # Solid relief (border)

style.configure("Treeview.Heading", 
                font=("Helvetica", 14, "bold"), 
                foreground="black", 
                background="#f7f6f9")

# Defining the columns
tree.heading("Key", text="Key")
tree.heading("Value", text="Value")

# Inserting the data with alternating row tags
for index, current_set in enumerate(info):
    for key, value in current_set.items():
        tag = 'evenrow' if index % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=(key, value), tags=(tag,))

# Packing the tree widget
tree.pack(fill="both", expand=True)

# Run the application
root.mainloop()
