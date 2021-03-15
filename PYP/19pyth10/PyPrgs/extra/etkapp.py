#!/usr/bin/python3
"""App-Modul für elegantere Tkinter-Anwendungen. Von App erben
und die vorhandenen Methoden überschreiben. Siehe ektpl_sample.py.
Diese Datei nicht verändern."""

import tkinter as tk
import os
import io
import base64

from PIL import Image, ImageTk

class App(tk.Frame):
    """Tkinter App-Klasse für Anwendungen, Vaterklasse. Ein Haupt-Frame
    mit umgebenden Menu, Buttonbar und Statusbar."""

    def __init__(self, master=None):
        """ init """
        tk.Frame.__init__(self, master)
        root = self._root()
        # main widgets
        self.create_widgets()
        # statusbar
        self.show_statusbar = tk.BooleanVar(value=True)
        self.show_statusbar.trace("w", self.update_show_statusbar)
        self.statusframe = tk.Frame(root)
        self.fill_statusbar()
        self.status('Ok')
        self.update_show_statusbar()
        # menubar
        self.menubar = tk.Menu(root)
        self.create_menubar()
        if self.menubar:
            root.config(menu=self.menubar)
        # buttonbar
        self.buttonbar = tk.Frame(root)
        self.create_buttonbar()
        if self.buttonbar:
            self.buttonbar.pack(side=tk.TOP, fill=tk.X)
        # das Haupt-Frame nimmt allen Platz ein
        self.pack(fill=tk.BOTH, expand=True)
        # Sauberes Beenden, wenn man auf Fenster-Schließen drückt
        root.protocol('WM_DELETE_WINDOW', self.endit)

    def not_implemented(self):
        """ noch nicht implementiert, dummy """
        print("Sorry, noch nicht implementiert für %s" % str(self))

    def create_widgets(self):
        """ Beispiel-Widgets. Überschreiben, aber kein super rufen """
        lbl = tk.Label(self, text='Override and fill self.create_widgets')
        lbl.grid(row=0, column=0)

    def fill_menubar(self, init):
        """ Menubar füllen von einer initialen Liste von MenuConfig's """
        for menuconfig in init:
            menuconfig.add_to(self.menubar)

    def create_menubar(self):
        """ Überschreiben, Vater nicht aufrufen aber fill_menubar """
        self.menubar = None # Default, keine Menubar

    def fill_buttonbar(self, init):
        """ Buttonbbar füllen von einer initialen Liste von ButtonConfig's """
        for button_config in init:
            button_config.add_to(self.buttonbar)

    def create_buttonbar(self):
        """ Überschreiben, Vater nicht aufrufen aber fill_buttonbar """
        self.buttonbar = None # Default, keine Buttonbar

    def fill_statusbar(self):
        """ Füllt die Statusbar. Kann überschrieben werden, dann super zuerst.
        Füge zu self.statusframe Elemente mit pack hinzu """
        self.statusbar = tk.Label(self.statusframe, bd=True,
                                  relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def status(self, message):
        """ Setzt Statusnachricht """
        self.statusbar['text'] = message

    def update_show_statusbar(self, *_):
        """ Aktualisiert Statusbar-Ansicht (Anzeige Ja/Nein) """
        if self.show_statusbar.get():
            self.statusframe.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            self.statusframe.pack_forget()

    def get_icon(self, *pos, **args):
        """ get icon """
        return get_icon(*pos, **args)

    def endit(self):
        """ Programmende. Super als letztes beim Überschreiben """
        self.show_statusbar.trace_vdelete(*self.show_statusbar.trace_vinfo()[0])
        self._root().quit()
        self._root().destroy()


SEPARATOR_STRING = 'separator'


class MenuConfig(object):
    """ Menu configuration
    Man braucht ein label und ein command. Das command can wieder ein
    MenuConfig sein, dann wird kaskadiert. Das command kann eine BooleanVar
    oder eine IntVar-Instanz sein, dann ist es ein CheckButton. Das
    command kann eine StringVar-Instanz sein, dann ist es ein RadioButton
    und es wird eine separater value-Parameter erwartet. Für den TopLevel
    wird alles aus den Labels ignoriert. """

    def __init__(self, label, command, **options):
        """ Initialisiere MenuConfig """
        self.label = label
        # Kann Liste von MenuConfigs sein oder Tk-Variable
        self.command = command
        self.accelerator = None
        self.compound = tk.LEFT
        self.image = None
        self.underline = None
        self.value = None
        for key in options:
            if key == "accelerator":
                self.accelerator = options[key]
            elif key == "compound":
                self.compound = options[key]
            elif key == "image":
                self.image = options[key]
            elif key == "underline":
                self.underline = options[key]
            elif key == "value":
                if not isinstance(self.command, tk.StringVar):
                    msg = "MenuConfig.__init__: value without StringVar"
                    raise ValueError(msg)
                self.value = options[key]
            else:
                msg = "MenuConfig.__init__: unknown option %s"
                raise ValueError(msg % key)
        if isinstance(self.command, tk.StringVar) and self.value is None:
            msg = "MenuConfig.__init__: StringVar without value"
            raise ValueError(msg)

    def _is_submenu(self):
        """ Check ob Untermenu """
        if self.command is None or isinstance(self.command, str): # may be?
            return False
        try:
            iter(self.command)
            return True
        except TypeError:
            return False

    def add_to(self, menu):
        """ Zu Menu hinzufügen """
        if self.label == SEPARATOR_STRING:
            menu.add_separator()
        elif self._is_submenu():
            # Sammlung von MenuConfigs, Untermenus
            submenu = tk.Menu(menu, tearoff=False)
            for menuconfig in self.command:
                menuconfig.add_to(submenu)
            menu.add_cascade(label=self.label, menu=submenu,
                             accelerator=self.accelerator,
                             compound=self.compound,
                             image=self.image,
                             underline=self.underline)
        elif isinstance(self.command, (tk.IntVar, tk.BooleanVar)):
            menu.add_checkbutton(label=self.label, variable=self.command,
                                 accelerator=self.accelerator,
                                 compound=self.compound,
                                 image=self.image,
                                 underline=self.underline)
        elif isinstance(self.command, tk.StringVar):
            menu.add_radiobutton(label=self.label, variable=self.command,
                                 accelerator=self.accelerator,
                                 compound=self.compound,
                                 image=self.image,
                                 underline=self.underline)
        else: # einzelnes command
            menu.add_command(label=self.label, command=self.command,
                             accelerator=self.accelerator,
                             compound=self.compound,
                             image=self.image,
                             underline=self.underline)

    def __repr__(self):
        """ Darstellung """
        what = "unknown"
        if self == MENU_SEPARATOR:
            what = SEPARATOR_STRING
        elif self._is_submenu():
            what = "submenu[%d]" % (len(self.command), )
        else:
            what = "menu"
        return "MenuConfig<%s>(%s)" % (what, self.label)

    __str__ = __repr__


EMBEDDED_ICONS = {
    "cut.png": 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAGBQTFRF////////vtnortLkn8PXiLbfdpCt7/T55ez1lMj6aHqbubvL1Or+weD9WWqK+fn7S1Vy5OXru9z9qKu+0dPbnqG3s9n8VGF5MjlnGyNOmp60ptL7jZGqWF6DQEhY3+jvDq7xtgAAAAF0Uk5TAEDm2GYAAAABYktHRACIBR1IAAAACXBIWXMAAABIAAAASABGyWs+AAAAkklEQVQY022P2xKDIAxETS0ERQEFxaDC//9lEa3tdLoPmdmTnVyq6p/grRs86vrJOOfwnUAhmvYiICV0fY+MqUJAm0HLbkTEA+S0Nc5MMM4zeshtNywLhezXFU0G26aIbPGrOEALgXbdnyCWxD7ICbJvmhTLDC6DPQHGskVsVueaEjqC61ClvIkxkoef7z7/3XoBD0gI+fHoCi4AAAAldEVYdGRhdGU6Y3JlYXRlADIwMTUtMTItMDdUMjI6NTg6MjQrMDE6MDAwvrSWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE1LTEyLTA3VDIyOjU4OjI0KzAxOjAwQeMMKgAAAABJRU5ErkJggg==',
    "copy.png": 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAGBQTFRF////////wdThr9Lln8TYibDKfaG8cpCu1+fw5e327PH2jsHvW3qex+P+qMvf8vb6vN39g7voVWuLs9n8VGJ7fKPAqtP7SFRpdrfpodD71dvklcr83+jvQUhXPURVKTFDaVmxmAAAAAF0Uk5TAEDm2GYAAAABYktHRACIBR1IAAAACXBIWXMAAABIAAAASABGyWs+AAAAj0lEQVQY003PSRKDMAxEUYQhjgyKDDgMYbr/LWkDrtA7vfobZZSW3aPcmKJ8WZuEzJvZMVf1XZFhkWdFHxXzrwCFShUr8Vo1LWVUqjSoIqgmQCXed50GwNf5Boi773UAWOfHCLgnPkH9iAowXVD/NEeFe56XNRZtG1Cd4DZAHCrmZXH5fn10VsOwbnu44bEDbuoKADd/7UgAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTUtMTItMDdUMjI6NTU6MjkrMDE6MDCkl17mAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE1LTEyLTA3VDIyOjU1OjI5KzAxOjAw1crmWgAAAABJRU5ErkJggg==',
    "paste.png": 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAGBQTFRF////////v4ol6sJeuZFIj2IU6qYg27Bi1adYvtnordHjn8TYiLHQdZWz4urz6/D2ksb4VmuJ6duwxuL98fb7/vno3c2fuNv90cGTptL7P0hb7ufSx7aG4NnH1dvky8zRPxtlUgAAAAF0Uk5TAEDm2GYAAAABYktHRACIBR1IAAAACXBIWXMAAABIAAAASABGyWs+AAAAhUlEQVQY02XP0QKCIAxGYQkxQ2BAS8Qs3/8t24Zcda72f3cbFHWT6BgopUejtZ6myYwN7spczR20fli7OO+96mADAIQQkxLI2cKTwuhI1PxaV4u0CyJ2WARK6bA55F0r7gIbA+8aBN7H4eEPeMfYIH+yxwYgQKUvBgpOBs6nlHYuyTsNr35ahgvV8D3JigAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxNS0xMi0wN1QyMjo1Nzo1NyswMTowMPqY/J8AAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTUtMTItMDdUMjI6NTc6NTcrMDE6MDCLxUQjAAAAAElFTkSuQmCC',
    "delete.png": 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAGBQTFRF/////////vj4/vb21EFG5hMT/sjI2t/nhKrFdJSx/lZW8PX65ez1ibvsV3CR8zIywuD9vN39/4iIUmF7ttr8sdf8qtT7SldtotD77fH1RE1fl8v84OjwP0ZWy8zRKTFD6/qXfQAAAAF0Uk5TAEDm2GYAAAABYktHRACIBR1IAAAACXBIWXMAAABIAAAASABGyWs+AAAAl0lEQVQY01XO2xKDIAwEUINSwSCKFwTB+v9/2QRsZ7pve9hh0oBoAQTUNBTRSXh1vVJKa80CIOUAiIYyWmAY5AQwz7PDkUVMEoaFwDlEXKFp5cLfUd+2nQHKvHZfQCF3qrv3eDxQnr0PpkDkPfUQgjkJdPz1lB/YKqSULwZ0354ig+0x0tmZEt83L6y163oc53lddz3sLx+qigyxUFI3yQAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxNS0xMi0wN1QyMzowNjowNSswMTowMGbk/SsAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTUtMTItMDdUMjM6MDY6MDUrMDE6MDAXuUWXAAAAAElFTkSuQmCC'
    }
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
ICON_DIRECTORY = os.path.join(CUR_DIR, "icons")
ICON_CACHE = dict() # keep a reference!
def get_icon(name):
    """ PNG-Icon von Icons-Verzeichnis oder embedded """
    if not name.endswith(".png"):
        name += ".png"
    if name in ICON_CACHE:
        return ICON_CACHE[name]
    filename = os.path.join(ICON_DIRECTORY, name)
    # override embedded
    if os.path.exists(filename):
        # race, but if, it should fail
        img = ImageTk.PhotoImage(Image.open(filename))
        ICON_CACHE[name] = img
        return ICON_CACHE[name]
    # last chance, embedded
    if name in EMBEDDED_ICONS:
        filehandle = io.BytesIO(base64.b64decode(EMBEDDED_ICONS[name]))
        openimage = Image.open(filehandle, mode='r')
        img = ImageTk.PhotoImage(image=openimage)
        ICON_CACHE[name] = img
        return ICON_CACHE[name]
    print("problem get_icon: %s" % name)
    return None


MENU_SEPARATOR = MenuConfig(SEPARATOR_STRING, None)
MenuConfig.SEPARATOR = MENU_SEPARATOR

class ButtonConfig(object):
    """ ButtonConfiguration
    Braucht ein command und entweder Bild oder Label oder beides.
    Es gibt kein Kaskadieren. """

    def __init__(self, command, **options):
        """ initialisiere ButtonConfig """
        self.command = command
        self.label = None
        self.image = None
        for key in options:
            if key == "label":
                self.label = options[key]
            elif key == "image":
                self.image = options[key]
            else:
                msg = "MenuConfig.__init__: unknown option %s"
                raise ValueError(msg % key)
        if self.label is None and self.image is None:
            msg = "ButtonConfig: both label and image mut not be None"
            raise Exception(msg)

    def add_to(self, widget):
        """ Hinzufügen des widgets mit pack """
        if self == BUTTON_SEPARATOR:
            button = tk.Label(widget, text="",
                              relief=tk.RAISED)
        elif self.label is not None:
            button = tk.Button(widget, command=self.command,
                               text=self.label)
        else: # Bild
            button = tk.Button(widget, command=self.command,
                               image=self.image)
        button.pack(side=tk.LEFT, fill=tk.Y)

    def __repr__(self):
        """ Darstellung """
        what = "unknown"
        if self == BUTTON_SEPARATOR:
            what = SEPARATOR_STRING
        elif self.label is not None:
            what = self.label
        else:
            what = "<image>"
        return "ButtonConfig(%s)" % (what)


BUTTON_SEPARATOR = ButtonConfig(None, label=SEPARATOR_STRING)
ButtonConfig.SEPARATOR = BUTTON_SEPARATOR

def main():
    "Immer so Instanzen in Main initialisieren und ausführen"
    app = App(tk.Tk())
    app._root().mainloop()

if __name__ == '__main__':
    main()
