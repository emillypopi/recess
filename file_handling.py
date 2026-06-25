"""Organize files in the Windows Downloads folder by extension."""

import argparse
import os
import shutil

DEFAULT_DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

EXTENSION_FOLDERS = {
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "ppt": "Documents",
    "pptx": "Documents",
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "tar": "Archives",
    "gz": "Archives",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "svg": "Images",
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "avi": "Videos",
    "mp3": "Audio",
    "wav": "Audio",
    "ogg": "Audio",
    "flac": "Audio",
    "py": "Code",
    "js": "Code",
    "ts": "Code",
    "html": "Code",
    "css": "Code",
    "json": "Code",
    "csv": "Data",
    "pptx": "Presentations",
}


def ensure_folder(path):
    os.makedirs(path, exist_ok=True)
    return path


def make_unique_path(dest_path):
    if not os.path.exists(dest_path):
        return dest_path

    base, ext = os.path.splitext(dest_path)
    counter = 1
    while True:
        new_path = f"{base} ({counter}){ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1


def organize_downloads(downloads_path):
    if not os.path.isdir(downloads_path):
        raise FileNotFoundError(f"Downloads folder not found: {downloads_path}")

    summary = {
        "moved": [],
        "skipped": [],
    }

    for entry in os.listdir(downloads_path):
        source_path = os.path.join(downloads_path, entry)
        if os.path.isdir(source_path):
            summary["skipped"].append({"path": source_path, "reason": "directory"})
            continue

        _, extension = os.path.splitext(entry)
        extension = extension.lower().lstrip(".")
        if not extension:
            target_folder_name = "No Extension"
        else:
            target_folder_name = EXTENSION_FOLDERS.get(extension, extension.upper())

        target_folder = ensure_folder(os.path.join(downloads_path, target_folder_name))
        destination_path = os.path.join(target_folder, entry)
        destination_path = make_unique_path(destination_path)

        shutil.move(source_path, destination_path)
        summary["moved"].append({
            "source": source_path,
            "destination": destination_path,
            "folder": target_folder_name,
        })

    return summary


def print_summary(summary):
    moved = summary["moved"]
    skipped = summary["skipped"]

    print(f"Moved {len(moved)} files.")
    for item in moved:
        print(f"  {os.path.basename(item['source'])} -> {item['folder']}/{os.path.basename(item['destination'])}")

    if skipped:
        print(f"Skipped {len(skipped)} items:")
        for item in skipped:
            print(f"  {item['path']} ({item['reason']})")


def main():
    parser = argparse.ArgumentParser(description="Organize files in the Downloads folder by extension.")
    parser.add_argument("--path", default=DEFAULT_DOWNLOADS, help="Path to the Downloads folder")
    args = parser.parse_args()

    downloads_path = os.path.abspath(args.path)
    print(f"Organizing files in: {downloads_path}")

    summary = organize_downloads(downloads_path)
    print_summary(summary)


if __name__ == "__main__":
    main()
