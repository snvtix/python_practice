import tkinter as tk

def calculate():
    distance = float(distance_var.get())
    calculation = round(distance*0.6241,2)
    label_ret = tk.Label(converter, text= calculation).grid(row=2, column=1, padx=5, pady=5)
    distance_var.set("")

converter = tk.Tk()
converter.title("Converter of distance units")

distance_var = tk.StringVar()

label_main = tk.Label(converter, text="Enter distance").grid(row=0, column=1, padx=5, pady=5)
label_miles = tk.Label(converter, text="Miles").grid(row=1, column=2, padx=5, pady=5)
label_km = tk.Label(converter, text="Kilometers").grid(row=2, column=2, padx=5, pady=5)

entry = tk.Entry(converter, textvariable=distance_var).grid(row=1, column=1)

button = tk.Button(converter, text="Calculate", command=calculate).grid(row=1, column=0)

converter.mainloop()