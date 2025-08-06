import os
import subprocess
import shutil

from . import Utils

from thonny import get_workbench, get_shell
from thonny import get_workbench
from tkinter import messagebox

from thonny import get_runner
from tkinter import filedialog


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


def check_mounting_points():
    print("🔍 Checking mount points for MicroPython mass storage...")
    mount_roots = ["/media", "/mnt", "/run/media"]
    for root in mount_roots:
        if os.path.isdir(root):
            print(f"  📂 Root: {root}")
            for sub in os.listdir(root):
                path = os.path.join(root, sub)
                print(f"    📁 Found: {path}")
                if os.path.isdir(path):
                    entries = os.listdir(path)
                    print(f"      📄 Contents: {entries}")
                    if "main.py" in entries or "boot.py" in entries:
                        print(f"✅ Found MicroPython device at: {path}")
                        return {"type": "micropython", "path": path, "ready": True}

def detect_micropython_device():
    """
    Detects a MicroPython device based on Thonny backend and mounted drives.

    Returns:
        {
            'type': 'micropython',
            'path': USB mount path if available, otherwise None,
            'ready': True or False
        }
    """
    try:
        runner = get_runner()
        backend_name = runner.get_backend_name().lower()
        if "micropython" in backend_name:
            # Try to find a mounted USB drive that looks like a MicroPython board
            mount_roots = ["/media", "/mnt", "/run/media"]
            for root in mount_roots:
                if os.path.isdir(root):
                    for sub in os.listdir(root):
                        path = os.path.join(root, sub)
                        if os.path.isdir(path):
                            entries = os.listdir(path)
                            if "main.py" in entries or "boot.py" in entries:
                                return {"type": "micropython", "path": path, "ready": True}
            # No mount found, but backend is active
            return {"type": "micropython", "path": None, "ready": True}
    except Exception as e:
        print(f"⚠️ Could not check Thonny backend: {e}")

    return {"type": None, "path": None, "ready": False}



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

