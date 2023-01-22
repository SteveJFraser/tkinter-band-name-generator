import tkinter as tk


root = tk.Tk()
root.geometry("600x250")


left_frame = tk.Frame(root, background="#1c1917", padx=50, pady=50)
left_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(root, background="#292524", padx=50, pady=50)
right_frame.pack(side="left", expand=True, fill="both")

# ========================================================================
# functions -----
def get_band():
    pass

# ========================================================================
# left side widgets

left_label = tk.Label(left_frame,
                      text="Enter the city you were born in",
                      background="#1c1917",
                      foreground="chartreuse",
                      font=("Arial", 10),
                      pady=10)
left_label.pack()

city_entry = tk.Entry(left_frame)
city_entry.pack()

left_label = tk.Label(left_frame,
                      text="Enter the name of your first pet",
                      background="#1c1917",
                      foreground="chartreuse",
                      font=("Arial", 10),
                      pady=10)
left_label.pack()

pet_entry = tk.Entry(left_frame)
pet_entry.pack()


# =========================================================================
# right side widgets
right_label = tk.Button(right_frame, text="Get Band Name", command=get_band)
right_label.pack()

band_name_label = tk.Label(right_label )
band_name_label.pack()

root.resizable(False,False)
root.mainloop()