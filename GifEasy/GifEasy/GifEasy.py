import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class gif_easy(tk.Label):
    def __init__(self, parent, gif, delay=20):
        super().__init__(parent)
        self.gif = Image.open(gif)
        self.original_frames = [frame.copy() for frame in ImageSequence.Iterator(self.gif)]
        self.frames = [ImageTk.PhotoImage(frame) for frame in self.original_frames]  # Garde les frames originales
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
        """Modifie l'apparence du GIF : arrière-plan et taille (sans casser l'animation)."""
        if bg:
            self.config(bg=bg)
            self.master.config(bg=bg)

        if size:
            x, y = size
            self.frames = [ImageTk.PhotoImage(frame.resize((x, y))) for frame in self.original_frames]  # Redimensionne chaque frame
            self.config(image=self.frames[0])  # Affiche la première frame redimensionnée
