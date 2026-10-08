import tkinter as tk

window = tk.Tk()
window.title("Penalty Shootout")
window.geometry("500x400")

title = tk.Label(window, text="⚽ Penalty Shootout", font=("Arial", 24))
title.pack(pady=30)

left_button = tk.Button(window, text="LEFT", width=15)
left_button.pack(pady=10)

centre_button = tk.Button(window, text="CENTRE", width=15)
centre_button.pack(pady=10)

right_button = tk.Button(window, text="RIGHT", width=15)
right_button.pack(pady=10)

window.mainloop()