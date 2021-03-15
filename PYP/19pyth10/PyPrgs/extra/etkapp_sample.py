#!/usr/bin/python3
"""Verwendung des eleganteren Tkinter-Templates.
Grundlage Ihres Programms"""

import tkinter as tk
from etkapp import App, MenuConfig, ButtonConfig


class MyApp(App):
    """Einfache Beispielanwendung; Zwei Eingabefelder, eine
    konsolidierte Anzeige und ein paar funktionslose Menus"""

    def __init__(self, master=None):
        """Initialisiere MyApp"""
        # Initialisiere die Anwendungslogik und UI-Logik
        self.wahl = tk.StringVar()
        self.wahl.set("Wahl3")
        # Alles bereit für die UI-Widgets und Darstellung
        App.__init__(self, master)
        # Abschließende Arbeiten
        self.status("Alles klar")

    def create_widgets(self):
        """Widgets"""
        tk.Label(self, text='Label 1:').grid(row=0, column=0)
        tk.Label(self, text='Label 2:').grid(row=1, column=0)
        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1, sticky=tk.W+tk.E)
        self.columnconfigure(1, weight=1)
        frame = tk.Frame(self)
        frame.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
        frame.columnconfigure(0, weight=1)
        self.lbl = tk.Label(frame, text="Eingabe: , ")
        self.lbl.grid(row=0, column=0, sticky=tk.W)
        btn = tk.Button(frame, text="Update", command=self.update)
        btn.grid(row=0, column=1)

    def create_menubar(self):
        """Meine MenuBar"""
        sni = self.not_implemented
        datei = [MenuConfig('Öffne', sni), MenuConfig('Speichere', sni),
                 MenuConfig.SEPARATOR, MenuConfig('Beende', self.endit)]
        teste = [MenuConfig("Test%d" % i, sni) for i in range(1, 6)]
        auswahl = [MenuConfig("Wahl%d" % i, self.wahl, value="wahl%d" %i)
                   for i in range(1, 6)]
        edit = [MenuConfig('Kopieren C', sni,
                           underline=9, image=self.get_icon("copy")),
                MenuConfig('Ausschneiden X', sni,
                           underline=13, image=self.get_icon("cut")),
                MenuConfig('Lösche D', self.delete,
                           underline=7, image=self.get_icon("delete")),
                MenuConfig.SEPARATOR,
                MenuConfig('Teste', teste),
                MenuConfig('Auswahl', auswahl),
                MenuConfig('Edit', sni),
               ]
        einstellungen = [MenuConfig('Zeige Status', self.show_statusbar),
                        ]
        hilfe = [MenuConfig('Bedienhilfe', sni),
                 MenuConfig('PyHilfe', sni),
                ]
        init = [MenuConfig('Datei', datei, underline=0),
                MenuConfig('Edit', edit, underline=0),
                MenuConfig('Einstellungen', einstellungen, underline=1),
                MenuConfig('Hilfe', hilfe, underline=0)
               ]
        self.fill_menubar(init)

    def create_buttonbar(self):
        """Meine ButtonBar"""
        sni = self.not_implemented
        init = [ButtonConfig(sni, label='Oeffne'),
                ButtonConfig(sni, label='Speichere'),
                ButtonConfig.SEPARATOR,
                ButtonConfig(sni, image=self.get_icon('copy')),
                ButtonConfig(sni, image=self.get_icon('cut')),
                ButtonConfig(self.delete, image=self.get_icon('delete')),
               ]
        self.fill_buttonbar(init)

    def delete(self):
        """GUI-Logik, lösche die Eingaben"""
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.update()
        self.mystatus("Eingaben gelöscht")

    def update(self):
        """GUI-Logik, aktualisiere Label aus Eingaben"""
        txt1 = self.entry1.get()
        txt2 = self.entry2.get()
        self.lbl["text"] = "Eingabe: %s, %s" % (txt1, txt2)
        self.mystatus("Eingabe-Anzeige aktualisiert")

    def mystatus(self, msg):
        """Mein Status, nach 2 Sekunden wieder Ok"""
        self.status(msg)
        self.after(2000, lambda: self.status("Ok"))


def main():
    "main"
    app = MyApp(tk.Tk())
    app._root().geometry('600x400') # Fenstergröße
    app._root().mainloop()

if __name__ == '__main__':
    main()
