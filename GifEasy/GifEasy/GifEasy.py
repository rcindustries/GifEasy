import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class gif_easy(tk.Label):
    def __init__(self, parent, gif, delay=20):
        super().__init__(parent)
        self.parent = parent
        self.gif_path = gif
        self.gif = Image.open(gif)
        self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.gif)]
        self.delay = int(delay * 1000)
        self.frame_index = 0
        self.running = False
        self.pack()

    def animate(self):
        if self.running:
            self.config(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.after(self.delay, self.animate)

    def start(self):
        if not self.running:
            self.running = True
            self.animate()

    def stop(self):
        self.running = False

    def style(self, bg=None, size=None):
        """Modifie l'apparence du GIF : arrière-plan et taille."""
        if bg:
            self.config(bg=bg)
            self.master.config(bg=bg)
        if size:
            x, y = size
            self.frames = [ImageTk.PhotoImage(frame.resize((x, y))) for frame in ImageSequence.Iterator(self.gif)]
            self.config(image=self.frames[0])

    def visible(self, state):
        """Affiche ou masque le GIF."""
        if state:
            self.pack()
        else:
            self.pack_forget()

    def change(self, gif):
        """Change le GIF affiché."""
        self.gif_path = gif
        self.gif = Image.open(gif)
        self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.gif)]
        self.config(image=self.frames[0])

    def destroy(self):
        """Supprime le GIF de l'affichage."""
        self.pack_forget()
        self.running = False
        self.destroy()