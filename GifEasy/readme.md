this is an tkinter easy package. allow You to make gif easily.


import tkinter as tk
from GifEasy import gif_easy

root = tk.Tk()
gif = gif_easy(root, gif="your_gif.gif", delay=0.05)
gif.style(bg="black")
gif.pack(padx=10, pady=20)
gif.start()

root.mainloop()

