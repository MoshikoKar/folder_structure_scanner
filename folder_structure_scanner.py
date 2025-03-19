import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to scan the folder and build the structure
def scan_folder_structure(folder_path):
    """
    Scan the folder and return a list of lines representing the folder structure.
    Excludes specified folders and file types.
    """
    # Excluded folder names and file extensions
    excluded_folders = {"node_modules", "__pycache__", "vnev", "backups", ".git"}
    excluded_extensions = {".db", ".ico"}
    
    structure_lines = [f"{os.path.basename(folder_path)}/"]
    
    def build_structure(root_dir, indent=""):
        nonlocal structure_lines
        # Get directories and files, excluding specified ones
        try:
            entries = os.listdir(root_dir)
        except PermissionError:
            return  # Skip directories we can't access
        
        dirs = []
        files = []
        for entry in entries:
            full_path = os.path.join(root_dir, entry)
            if os.path.isdir(full_path):
                if entry not in excluded_folders:
                    dirs.append(entry)
            elif os.path.isfile(full_path) and not any(entry.endswith(ext) for ext in excluded_extensions):
                files.append(entry)
        
        # Sort for consistent output
        dirs.sort()
        files.sort()
        
        # Process directories and files
        for i, dir_name in enumerate(dirs):
            is_last = (i == len(dirs) - 1 and not files)
            prefix = "└──" if is_last else "├──"
            structure_lines.append(f"{indent}{prefix} {dir_name}/")
            build_structure(os.path.join(root_dir, dir_name), indent + ("    " if is_last else "│   "))
        
        for i, file_name in enumerate(files):
            is_last = (i == len(files) - 1)
            prefix = "└──" if is_last else "├──"
            structure_lines.append(f"{indent}{prefix} {file_name}")
    
    # Start building from the root
    build_structure(folder_path, "│   ")
    return structure_lines

# GUI functions
def select_folder():
    """Open a dialog to select the folder to scan."""
    folder = filedialog.askdirectory()
    if folder:
        selected_folder.set(folder)

def run_scan():
    """Scan the selected folder and generate a structure file."""
    folder = selected_folder.get()
    
    # Validate input
    if not folder:
        messagebox.showerror("Error", "Please select a folder to scan.")
        return
    
    try:
        # Get the folder structure
        structure_lines = scan_folder_structure(folder)
        
        # Write to output file
        with open('folder_structure.txt', 'w', encoding='utf-8') as f:
            f.write("\n".join(structure_lines))
        
        messagebox.showinfo("Done", "Folder structure generated: folder_structure.txt")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while scanning: {str(e)}")

# Set up the GUI
root = tk.Tk()
root.title("Folder Structure Scanner")

# Variable to store the selected folder
selected_folder = tk.StringVar()

# Folder selection UI
tk.Label(root, text="Select folder to scan for structure:").pack(pady=5)
tk.Button(root, text="Browse", command=select_folder).pack()
tk.Label(root, textvariable=selected_folder).pack()

# Scan button
tk.Button(root, text="Generate Folder Structure", command=run_scan).pack(pady=10)

# Start the GUI event loop
root.mainloop()