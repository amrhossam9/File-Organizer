# File-Organizer

This script organizes files in a given folder by **MIME type** into subfolders such as `Image`, `Video`, `Text`, `Application`, and `Unknown`.

### Requirements

* Python
* No external dependencies (uses standard library)

---

### How to Run

1. **Clone the repo**.

2. **Open a terminal** in the folder containing the script.

3. **Run the script** with:

   ```bash
   python file_organizer.py <folder_path>
   ```

   Example:

   ```bash
   python organize_files.py "C:/Users/Amr/Desktop/Stuff"
   ```

---

### Optional: Simulation Mode

If you want to **preview** what will happen without moving files:

```bash
python organize_files.py "C:/Users/Amr/Desktop/Stuff" --simulate
```

---

### How It Works

1. Scans **only the given folder** (no subfolders).
2. Determines file type using **MIME types**.
3. Creates a subfolder for each type if it doesn’t exist.
4. Moves files into the correct subfolder.
5. Prints a summary of how many files went into each category.
