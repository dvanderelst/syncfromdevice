from thonny import get_workbench, get_shell
from tkinter import messagebox
import os
from . import Utils
from . import Sync


def load_plugin():
    print("✅ myplugin loaded!")
    fallback_path = None  # fallback origin folder
    target_folder = None  # destination folder

    def hello():
        nonlocal fallback_path, target_folder
        origin_info = Utils.detect_python_device()
        parent = get_workbench()

        if not origin_info["ready"]:
            if fallback_path is None:
                header = "Fallback Mode"
                message = "No device found. Select a local folder as origin."
                messagebox.showinfo(header, message, parent=parent)
                print("⚠️", header, message)
                fallback_path = Utils.ask_folder('Select origin folder')
            Utils.change_path(fallback_path)
            origin_info = {"type": "local", "path": fallback_path, "ready": True}
        else:
            header = "Device Detected"
            message = f"Connected to {origin_info['type']} device."
            messagebox.showinfo(header, message, parent=parent)
            print("✅", header, message)

        if target_folder is None:
            header = "Select Target Folder"
            message = "Select a target folder."
            messagebox.showinfo(header, message, parent=parent)
            print("⚠️", header, message)
            target_folder = Utils.ask_folder('Select target folder')

        # Ready to proceed with syncing
        Utils.log_to_console('Starting sync...')
        origin_string = "Origin: " + origin_info["path"]
        target_string = "Target: " + target_folder
        print(origin_string)
        print(target_string)
        Utils.log_to_console(origin_string)
        Utils.log_to_console(target_string)


        try:
            Sync.sync_folders(origin_info["path"], target_folder)
            Utils.log_to_console("Sync complete.")
        except Exception as e:
            Utils.log_to_console(f"Sync failed: {e}")


    workbench = get_workbench()
    workbench.add_command(
        "sync_files", 
        "tools", 
        "Sync from device", hello, 
        group=180, 
        accelerator="Ctrl+Shift+Y",         # For display in the menu
        default_sequence="<Control-Shift-Y>"  # For actual key binding
        )
