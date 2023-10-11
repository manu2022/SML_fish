import tkinter as tk
import numpy as np

# Coefficients and intercepts for each fish species
coefficients = {
    'Bream': [0.95967231, 1.09558416, 0.7350255],
    'Roach': [1.248582, 0.26414403, 1.31365923],
    'Whitefish': [0.46007613, 3.50356937, -0.56108943],
    'Parkki': [-0.21333294, 0.71909932, 2.07651168],
    'Perch': [1.55142697, 0.83504915, 0.54233029],
    'Pike': [1.42384013, 0.73041239, 0.77476223],
    'Smelt': [1.04111787, 1.13896483, 0.33074863],
}

intercepts = {
    'Bream': -0.4842069983879198,
    'Roach': -0.43981470045981563,
    'Whitefish': -1.09127685685031,
    'Parkki': 0.6935026323582756,
    'Perch': -0.8483199292220611,
    'Pike': -0.7403711582151922,
    'Smelt': -0.503420454163209,
}

def calculate_weight():
    fish_category = fish_var.get()
    length = float(length_entry.get())
    height = float(height_entry.get())
    width = float(width_entry.get())
    
    coefficients_species = coefficients.get(fish_category, [0, 0, 0])
    intercept_species = intercepts.get(fish_category, 0)
    
    weight = 10 ** (intercept_species + coefficients_species[0] *  np.log10(length) + coefficients_species[1] *  np.log10(height) + coefficients_species[2] * np.log10(width))
    
    # Take the logarithm base 10 of the weight
    
    
    result_label.config(text=f"Weight (log10): {weight:.2f} units")

# Create the main window
root = tk.Tk()
root.title("Fish Weight Calculator")

# Create labels and entry boxes for length, height, and width
length_label = tk.Label(root, text="Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

# Create a dropdown menu for fish categories
fish_var = tk.StringVar(root)
fish_var.set("Bream")  # Default value
fish_label = tk.Label(root, text="Fish Category:")
fish_label.pack()
fish_menu = tk.OptionMenu(root, fish_var, *coefficients.keys())
fish_menu.pack()

# Create a button to calculate weight
calculate_button = tk.Button(root, text="Calculate Weight", command=calculate_weight)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()
