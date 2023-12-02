import tkinter as tk
from tkinter import ttk

def populate_treeview(tree):
    # Inserting sample data into the treeview
    data = [
        ("NIck", "Annual Leave", "Approved"),
        ("Smith", "Sick Leave", "Pending"),
        ("Johnson", "Personal Leave", "Rejected"),
         ("peter", "casual leave", "pending"),
            ("helly", "sick leave", "Pending"),
               ("peter", "casual leave", "Pending"),
                  ("peter", "sick leave", "Aproved"),
                           ("NIck", "Annual Leave", "Approved"),
        ("Smith", "Sick Leave", "Pending"),
        ("Johnson", "Personal Leave", "Rejected"),
         ("peter", "casual leave", "pending"),
            ("helly", "sick leave", "Pending"),
               ("peter", "casual leave", "Pending"),
                  ("peter", "sick leave", "Aproved"),
    ]

    for record in data:
        tree.insert("", "end", values=record)

def add_leave():
    # Implement functionality to add a leave record
    pass

def edit_leave():
    # Implement functionality to edit a leave record
    pass

def delete_leave():
    # Implement functionality to delete a leave record
    pass

root = tk.Tk()
root.title("Leave Status Management")

# Creating a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Type", "Status"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Type", text="Type")
tree.heading("Status", text="Status")

# Adjusting column widths
tree.column("Name", width=150,)
tree.column("Type", width=150)
tree.column("Status", width=100)

# Inserting data into the treeview
populate_treeview(tree)

# Packing the Treeview
tree.pack(padx=10, pady=10)

# Buttons for actions
add_button = ttk.Button(root, text="Add Leave", command=add_leave)
add_button.pack()

edit_button = ttk.Button(root, text="Edit Leave", command=edit_leave)
edit_button.pack()

delete_button = ttk.Button(root, text="Delete Leave", command=delete_leave)
delete_button.pack()

root.mainloop()