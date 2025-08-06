import os
import shutil

def sync_folders(origin, target, subfolder='device_sync', exclude_hidden=True):
    """
    Syncs contents of 'origin' to a subfolder inside 'target'.
    The subfolder will be cleared and then filled with origin's contents.
    
    Parameters:
        origin (str): Source folder path.
        target (str): Destination folder path.
        subfolder (str): Subfolder inside 'target' to sync to. Defaults to 'device_sync'.
        exclude_hidden (bool): Whether to ignore hidden files/folders.
    """
    if not os.path.isdir(origin) or not os.path.isdir(target):
        raise ValueError("Both origin and target must be valid directories.")
    
    sync_path = os.path.join(target, subfolder)

    if os.path.abspath(origin) == os.path.abspath(sync_path):
        raise ValueError("Origin and destination subfolder must be different.")

    os.makedirs(sync_path, exist_ok=True)

    for entry in os.scandir(sync_path):
        if exclude_hidden and entry.name.startswith('.'):
            continue
        try:
            if entry.is_dir():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)
        except Exception as e:
            print(f"Error removing {entry.path}: {e}")

    for entry in os.scandir(origin):
        if exclude_hidden and entry.name.startswith('.'):
            continue
        src = entry.path
        dst = os.path.join(sync_path, entry.name)
        try:
            if entry.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)
        except Exception as e:
            print(f"Error copying {src} to {dst}: {e}")
