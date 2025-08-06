import os
import shutil

def sync_folders(origin, target, exclude_hidden=True):
    """
    Replaces all contents of 'target' with contents of 'origin'.
    """
    if not os.path.isdir(origin) or not os.path.isdir(target):
        raise ValueError("Both origin and target must be valid directories.")

    if os.path.abspath(origin) == os.path.abspath(target):
        raise ValueError("Origin and target folders must be different.")

    # Clear target
    for item in os.listdir(target):
        if exclude_hidden and item.startswith('.'):
            continue
        item_path = os.path.join(target, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

    # Copy all from origin to target
    for item in os.listdir(origin):
        if exclude_hidden and item.startswith('.'):
            continue
        src_path = os.path.join(origin, item)
        dst_path = os.path.join(target, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)
