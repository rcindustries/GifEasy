import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class gif_easy(tk.Label):
    def __init__(self, parent, gif, delay=20):
        super().__init__(parent)
        self.gif = Image.open(gif)
        self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.gif)]
        self.delay = int(delay * 1000)  # Convertit les secondes en millisecondes
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

    def style(self, bg=None, fg=None, border=None):
        """Modifie le style du GIF : arrière-plan, texte et bordure."""
        if bg:
            self.config(bg=bg)  # Change l'arrière-plan du widget
            self.master.config(bg=bg)  # Change l'arrière-plan de la fenêtre principale
        if fg:
            self.config(fg=fg)  # Change la couleur du texte si besoin
        if border:
            self.config(borderwidth=border)  # Change la largeur de la bordure