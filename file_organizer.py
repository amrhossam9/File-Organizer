import argparse
from collections import defaultdict
import mimetypes
from pathlib import Path
import shutil

def get_category(file_path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(file_path.name)
    if mime_type:
        return mime_type.split("/")[0].capitalize()
    return "Unknown"

def organize_files(folder_path: Path, simulate: bool = False):
    if not folder_path.exists():
        print(f"Error: '{folder_path}' is not a valid folder.")
        return

    summary = defaultdict(int)

    for file in folder_path.iterdir():
        if file.is_dir():
            continue

        category = get_category(file)
        target_dir = folder_path / category
    
        if not target_dir.exists() and not simulate:
                target_dir.mkdir()

        target_path = target_dir / file.name

        if simulate:
            print(f"[SIMULATE] Move '{file.name}' → '{category}/'")
        else:
            shutil.move(str(file), str(target_path))

        summary[category] += 1

    print("\nSummary:")
    for category, count in sorted(summary.items()):
        print(f"{category}: {count} file(s)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that organizes files in a given folder by file type.")
    parser.add_argument("folder", type=Path, help="Path to the folder to organize")
    parser.add_argument("--simulate", action="store_true", help="Simulate mode that shows what would happen without moving files.")
    args = parser.parse_args()

    organize_files(args.folder, args.simulate)

