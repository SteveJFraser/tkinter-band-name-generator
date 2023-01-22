import tkinter as tk

# =======================================================================
# window configurations --------
root = tk.Tk()
root.geometry("800x250")
root.resizable(False, False)
root.title("👨‍💻 Band name generator")
left_frame = tk.Frame(root, background="#1c1917", padx=50, pady=50)
left_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(root, background="#292524", padx=90, pady=50)
right_frame.pack(side="left", expand=True, fill="both")

# ========================================================================
# entry variables
city = tk.StringVar()
pet = tk.StringVar()


# ========================================================================
# functions -----
def get_band(*args):
    city_name = city.get()
    pet_name = pet.get()
    if city_name and pet_name:
        band_name_label.config(text=f"{city_name} {pet_name}")
    else:
        band_name_label.config(text="Band Name")


# ========================================================================
# left side widgets
left_label = tk.Label(left_frame,
                      text="Enter the city you were born in", background="#1c1917",
                      foreground="#a8a29e", font=("Arial", 14), pady=10)
left_label.pack()
city_entry = tk.Entry(left_frame, textvariable=city, width=20,
                      font=("Arial", 14))
city_entry.pack()
left_label = tk.Label(left_frame,
                      text="Enter the name of your first pet",background="#1c1917",
                      foreground="#a8a29e",font=("Arial", 14),pady=10)
left_label.pack()
pet_entry = tk.Entry(left_frame, textvariable=pet, width=20,
                     font=("Arial", 14))
pet_entry.pack()
# =========================================================================
# right side widgets
band_name_btn = tk.Button(right_frame,
                          text="Get Band Name",
                          command=get_band, pady=10, background="#a8a29e")
band_name_btn.pack()
quit_button = tk.Button(right_frame,
                        text="Quit",
                        command=root.destroy, padx=31, pady=10, background="#a8a29e")
quit_button.pack(side="bottom")

band_name_label = tk.Label(right_frame, text="Band Name",
                           background="#292524", foreground="#4338ca",
                           font=("Arial", 15), pady=20)
band_name_label.pack(side="bottom")

root.bind("<Return>", get_band)

root.mainloop()
