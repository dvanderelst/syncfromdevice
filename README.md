

**STATUS: HAS NOT BEEN TESTED WITH A MICROCONTROLLER BOARD**

# Thonny Plugin: Sync from Device

This Thonny plugin adds a menu item and keyboard shortcut to quickly sync files from a connected MicroPython/CircuitPython device, or from a local folder if no device is detected. It replaces the contents of a selected target folder with the contents of the origin (device or folder).

## Thonny Version

This plugin was developed for Thonny 4.1.4. This can be downloaded from the Thonny website.
**Remove existing 3.x versions from your system.**

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

## 📦 Installing `mpremote` in Thonny's Python Environment

This plugin uses [`mpremote`](https://pypi.org/project/mpremote/) to connect to MicroPython devices.

To work correctly, `mpremote` must be installed **into the same Python environment that Thonny uses**.

---

### 🧭 Step-by-Step Installation

1. ### 🧩 Select the *Local Python Interpreter* in Thonny

   In Thonny:
   - Go to **Tools → Options → Interpreter**
   - Select:
     ```
     The same interpreter which runs Thonny (default)
     ```
   - Click **OK**

2. ### 💻 Open the *System Shell* from Thonny

   - Go to **Tools → Open system shell**

   You will see a message like this:

   ```
   ********************************************************************************
   Some Python commands in the PATH of this session:
    - python3   -> /home/yourname/apps/thonny/bin/python3.10
    - pip3      -> /home/yourname/apps/thonny/bin/pip3.10
   ```

   > ✅ This means you're now using the same Python and `pip3` that Thonny uses.

3. ### 📥 Install `mpremote` into Thonny's Python

   In the **system shell** you just opened, run:

   ```bash
   pip3 install mpremote
   ```

4. ### ✅ Verify the Installation in Thonny

   Back in the Thonny **Python shell**, type:

   ```python
   import shutil
   print(shutil.which("mpremote"))
   ```

   You should see something like:

   ```
   /home/yourname/apps/thonny/bin/mpremote
   ```

   If it prints `None`, `mpremote` was not installed correctly into Thonny’s environment. Try repeating Step 3 and ensure you're using the correct shell.

---

### 💡 Tip

Avoid using `pip3` from your regular terminal unless you're **absolutely sure** it's using Thonny’s Python. Always prefer using **Tools → Open system shell** from within Thonny to install packages for plugins like this one.


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


