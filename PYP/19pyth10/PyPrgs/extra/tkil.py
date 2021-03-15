"""Helper that provides a main function running your GUI class.
It includes a mainloop with a thread safe way to call functions
from a background thread with invoke_later.
Do not use for animations, only for a standard background GUI tasks,
as the queue is only checked periodically."""

import tkinter
import queue
import threading

_queue = queue.Queue()
_done = threading.Event()
def _event_loop(root):
    if not _done.is_set():
        try:
            while True: # drain the queue
                fun = _queue.get_nowait()
                fun()
        except queue.Empty:
            pass
        # do again after 100 msecs
        root.after(100, lambda: _event_loop(root))


def invoke_later(fun, *posargs, **kwargs):
    "call to run fun with given args in the main GUI thread"
    dofun = lambda: fun(*posargs, **kwargs)
    _queue.put(dofun)


def main(Main, *posargs, **kwargs):
    """main function, provide a Main GUI class to instantiate
    that accepts a root, all args are forwarded
    """
    root = tkinter.Tk()
    posargs = (root, *posargs)
    _main = Main(*posargs, **kwargs) # keep reference
    _event_loop(root) # establish event queue loop
    root.mainloop() # here we block
    _done.set() # finish event queue loop
