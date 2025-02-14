import tkinter as tk
from tkinter import ttk

# Pressure unit conversion dictionary
pressure_units = {
    "Pa": 1, "kPa": 1e3, "MPa": 1e6, "bar": 1e5, "mbar": 1e2, "atm": 101325,
    "cmH2O": 98.0665, "mmH2O": 9.80665, "inH2O": 249.0889, "ftH2O": 2988.98,
    "mmHg": 133.322, "inHg": 3386.39, "psi": 6894.76, "psf": 47.88,
    "Torr": 133.322, "microns": 0.133322, "mTorr": 0.133322
}

# Function to convert pressure
def convert_pressure():
    try:
        value = float(entry_value.get())
        input_unit = combo_input.get()
        output_unit = combo_output.get()
        
        # Convert to Pascal first, then to output unit
        value_in_pa = value * pressure_units[input_unit]
        converted_value = value_in_pa / pressure_units[output_unit]
        
        label_result.config(text=f"Result: {converted_value:.5f} {output_unit}", font=("Arial", 18, "bold"))
    except ValueError:
        label_result.config(text="Invalid input! Enter a number.", font=("Arial", 18, "bold"))

# Create main window
root = tk.Tk()
root.title("Pressure Unit Converter")
root.geometry("1920x1080")  # Increase window size
root.configure(bg="#f0f0f0")  # Set background color

# Styling
label_font = ("Arial", 18, "bold")
entry_font = ("Arial", 18)
button_font = ("Arial", 18, "bold")

# Input field
tk.Label(root, text="Enter Pressure Value:", font=label_font, bg="#f0f0f0").pack(pady=5)
entry_value = tk.Entry(root, font=entry_font, width=15, justify='center')
entry_value.pack(pady=5)

# Input unit selection
tk.Label(root, text="Select Input Unit:", font=label_font, bg="#f0f0f0").pack()
combo_input = ttk.Combobox(root, values=list(pressure_units.keys()), font=entry_font, state="readonly")
combo_input.pack()
combo_input.current(0)

# Output unit selection
tk.Label(root, text="Select Output Unit:", font=label_font, bg="#f0f0f0").pack()
combo_output = ttk.Combobox(root, values=list(pressure_units.keys()), font=entry_font, state="readonly")
combo_output.pack()
combo_output.current(1)

# Convert button
convert_button = tk.Button(root, text="Convert", font=button_font, bg="#0078D7", fg="white", width=15, height=2, command=convert_pressure)
convert_button.pack(pady=15)

# Result label
label_result = tk.Label(root, text="Result: ", font=label_font, bg="#f0f0f0")
label_result.pack(pady=10)

# Run the application
root.mainloop()
