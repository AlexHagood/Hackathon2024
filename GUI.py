import tkinter as tk
from tkinter import ttk
import random

def rPrice():
    return f"${random.randint(0, 20) + round(random.random(), 2)}"
def calculatePrice():
    # Clear the existing content in the Treeview
    for item in tree.get_children():
        tree.delete(item)

    groceryList = listEntry.get("1.0", "end-1c")
    print(groceryList)
    groceryList = groceryList.split("\n")
    
    data = []
    column_sums = [0, 0, 0, 0]  # Initialize sums for each column

    for item in groceryList:
        if item.strip():  # Skip empty lines
            row_values = (item, rPrice(), rPrice(), rPrice())
            data.append(row_values)

            # Update column sums
            for i in range(1, len(row_values)):
                column_sums[i-1] += float(row_values[i][1:])

    for row in data:
        tree.insert("", "end", values=row)

    # Add the bottom row with column sums
    bottom_row_values = ("Total", f"${column_sums[0]:.2f}", f"${column_sums[1]:.2f}", f"${column_sums[2]:.2f}")
    tree.insert("", "end", values=bottom_row_values, tags='sum_row')

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Grocery Shopper")

# Set the window size
window.geometry("800x800")

# Create a Treeview widget outside the function
tree = ttk.Treeview(window, columns=("Item", "Roseaurs", "Safeway", "Walmart"), show="headings")
tree.heading("Item", text="Item")
tree.heading("Roseaurs", text="Roseaurs")
tree.heading("Safeway", text="Safeway")
tree.heading("Walmart", text="Walmart")

# Add a tag to the bottom row for styling
tree.tag_configure('sum_row', background='grey')

# Create a label widget
listEntry = tk.Text(window, font=("Helvetica", 16))
calculateButton = tk.Button(window, text="Calculate prices", command=calculatePrice)

# Pack the label and button into the window
listEntry.pack(pady=5)
calculateButton.pack()

# Pack the Treeview widget into the window
tree.pack()

# Run the Tkinter event loop
window.mainloop()
