import os
import subprocess
from thonny import get_workbench
from tkinter import messagebox
from . import Utils
import os
from thonny import get_runner

from tkinter import filedialog
from thonny import get_workbench, get_shell

import os
from tkinter import filedialog
from thonny import get_workbench

def ask_folder(title="Select folder"):
    """
    Prompts the user to select a folder.
    Starts in the user's home directory.
    Returns the absolute path or None if cancelled.
    """
    initial = os.path.expanduser("~")
    folder = filedialog.askdirectory(parent=get_workbench(), title=title, initialdir=initial)
    if not folder:
        return None
    return os.path.abspath(folder)


def change_path(path):
    """
    Sends a %cd command to the Thonny shell to change its working directory.
    """
    capture = f"%cd {path}"
    get_shell().submit_magic_command(capture)


def log_to_console(*lines):
    """
    Print one or more lines directly to the Thonny Shell console.
    Auto-scrolls to the bottom.
    """
    shell = get_shell()
    for line in lines:
        shell.text.insert("end", f"{line}\n")
    shell.text.see("end")


def detect_circuitpython_device():
    """
    Detects a mounted CircuitPython device by looking for 'boot_out.txt' 
    in common mount locations. Returns the mount path if found.
    """
    mount_roots = ["/media", "/mnt", "/run/media"]

    for root in mount_roots:
        if os.path.isdir(root):
            for sub in os.listdir(root):
                path = os.path.join(root, sub)
                if os.path.isdir(path) and os.path.exists(os.path.join(path, "boot_out.txt")):
                    return path

    return None

def detect_micropython_device():
    """
    Checks if a MicroPython device is accessible via `mpremote connect auto`.
    Returns True if found, False otherwise.
    """
    try:
        subprocess.run(
            ["mpremote", "connect", "auto"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except Exception:
        return False

def detect_python_device():
    """
    Detects whether a CircuitPython or MicroPython device is connected.
    Returns a dictionary:
        {
            'type': 'circuitpython' | 'micropython' | None,
            'path': mount path (for CircuitPython) or None,
            'ready': True | False
        }
    """
    cp_path = detect_circuitpython_device()
    if cp_path:
        return {"type": "circuitpython", "path": cp_path, "ready": True}

    if detect_micropython_device():
        return {"type": "micropython", "path": None, "ready": True}

    return {"type": None, "path": None, "ready": False}

