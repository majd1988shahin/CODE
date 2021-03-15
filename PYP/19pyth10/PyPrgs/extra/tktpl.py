#!/usr/bin/python3
"""Einfaches Tkinter-Template"""

import tkinter as tk


class Greetings:
    "Die Anwendungslogik gekapselt"

    GREETINGS = ["Hallo", "Hello", "Aloita", "Oi", "Ni Hao"]

    def __init__(self):
        self.idx = 0

    def next(self):
        "naechster Gruss"
        self.idx = (self.idx + 1) % len(self.GREETINGS)

    def _get_greeting(self):
        "Lesezugriff auf Gruss"
        return self.GREETINGS[self.idx]

    greet = property(_get_greeting, None, None, "greet")


class Main(tk.Frame):
    "Das UI gekapselt"

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.greetings = Greetings() # initialisiere die Anwendungsinstanz
        self.create_widgets()
        self._root().protocol('WM_DELETE_WINDOW', self.endit)

    def create_widgets(self):
        "erzeuge alle Widgets"
        self.label = tk.Label(self, text=self.greetings.greet)
        self.label.pack()
        btn_frame = tk.Frame(self)
        btn_frame.pack()
        gruss = tk.Button(btn_frame, text="Grüße",
                          command=self.change_gruss)
        gruss.pack(side=tk.LEFT)
        beende = tk.Button(btn_frame, text="Beenden",
                           command=self.endit)
        beende["fg"] = "red"
        beende.pack(side=tk.LEFT)

    def change_gruss(self):
        "Grusswechsel, ausgeloest durch Button"
        self.greetings.next()
        self.label["text"] = self.greetings.greet

    def endit(self):
        "Beende die Anwendung sauber"
        self._root().quit()
        self._root().destroy()

def main():
    "main"
    root = tk.Tk()
    _main = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
