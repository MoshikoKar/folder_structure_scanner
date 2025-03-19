# Folder Structure Scanner

## Description
This Python script offers a GUI tool to scan a selected folder and generate a tree-like representation of its directory structure. It excludes specific folders and file types during the scan and writes the result to a `folder_structure.txt` file. The script is useful for documenting a project’s folder layout while ignoring common development-related directories and files.

## Features
- Scans a folder and its subfolders to build a tree structure.
- Excludes the following folders and their contents: `node_modules`, `__pycache__`, `vnev`, `backups`, `.git`.
- Excludes files with extensions: `.db`, `.ico`.
- Outputs the structure to `folder_structure.txt` with a tree-like format using `├──` and `└──`.
- Simple GUI with a "Browse" button to select the folder.

## Requirements
- Python 3.x
- Tkinter (usually included with Python; install via `pip install tk` if missing)

## Usage
1. **Run the Script**:
   - Save the script as `folder_structure_scanner.py`.
   - Execute it with Python: `python folder_structure_scanner.py`.
   - A GUI window titled "Folder Structure Scanner" will appear.

2. **Select a Folder**:
   - Click the "Browse" button next to "Select folder to scan for structure".
   - Choose the folder you want to scan (e.g., `C:\myproject`).

3. **Generate the Structure**:
   - Click "Generate Folder Structure".
   - The script will scan the folder and create `folder_structure.txt` in the same directory as the script.

4. **View Results**:
   - Open `folder_structure.txt` to see the folder structure.
   - Example output:
     ```
     myproject/
     │   ├── backend/
     │   │   ├── .env
     │   │   └── server.js
     │   └── frontend/
     │       └── App.js
     ```

## Exclusions
- **Folders**: `node_modules`, `__pycache__`, `vnev`, `backups`, `.git` (and all their subfolders/files) are skipped.
- **File Types**: Files ending with `.db` (e.g., `data.db`) or `.ico` (e.g., `icon.ico`) are ignored.

## Notes
- **Tree Format**: Uses `├──` for branches and `└──` for the last item at each level, with `│   ` or spaces for indentation.
- **Relative Names**: The structure is rooted at the selected folder’s base name (e.g., `myproject/`), with subpaths relative to it.
- **Error Handling**: Skips inaccessible directories (e.g., due to permissions) and displays a message box for other errors.
- **Customization**: To exclude additional folders or file types, modify the `excluded_folders` or `excluded_extensions` sets in the `scan_folder_structure` function.

## License
This script is provided as-is for personal or educational use. Feel free to modify it to suit your needs!
