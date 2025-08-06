
# Thonny Plugin: Sync from Device

This Thonny plugin adds a menu item and keyboard shortcut to quickly sync files from a connected MicroPython/CircuitPython device, or from a local folder if no device is detected. It replaces the contents of a selected target folder with the contents of the origin (device or folder).

## 🚀 Features

- Detects and uses connected MicroPython/CircuitPython devices
- Falls back to user-selected local folder if no device is connected
- Asks for a target folder only once per session
- Deletes all existing files in the target folder before syncing
- Provides feedback in both the GUI and the Thonny Shell
- Adds a Tools menu item and supports a customizable shortcut (`Ctrl+Shift+Y` by default)

---

## 📦 Installation

1. Clone or download this repository.
2. Place the plugin folder (e.g., `syncfromdevice`) in:

   ```
   ~/.config/Thonny/plugins/lib/python3.x/site-packages/thonnycontrib/
   ```

   Example:

   ```
   /home/dieter/.config/Thonny/plugins/lib/python3.10/site-packages/thonnycontrib/syncfromdevice
   ```

3. Restart Thonny.

> 🔧 If the `thonnycontrib` folder doesn't exist, create it manually. This is where Thonny discovers community plugins.

---

## ⌨️ Usage

- Open Thonny
- Go to **Tools → Sync from device** or press **Ctrl+Shift+Y**
- If a device is connected, it will use it as the source
- If no device is detected, you’ll be asked to choose a source folder
- You'll also be asked once per session to select a destination folder
- The contents of the destination will be replaced with the origin

---

## 🧠 Notes

- Hidden files and folders (starting with `.`) are ignored during sync
- Origin and target paths are remembered while Thonny stays open
- You can customize or rebind the shortcut in **Tools → Options → Keybindings**

---


