# cli_runner.py
# Created to execute selected Python programs from 'Programs/' folder and its subfolders
# Author: Shresth Dwivedi

import os
import time
import sys
import io
import traceback
from contextlib import redirect_stdout

try:
    from colorama import init, Fore
except ImportError:
    os.system("pip install colorama")
    from colorama import init, Fore

init(autoreset=True)

PROGRAM_FOLDER = "Programs"
EXT = ".py"
SEPARATOR = "-" * 40

def list_programs():
    all_files = []
    for root, _, files in os.walk(PROGRAM_FOLDER):
        for file in files:
            if file.endswith(EXT):
                rel_path = os.path.relpath(os.path.join(root, file), PROGRAM_FOLDER)
                all_files.append(rel_path)
    return sorted(all_files)

def print_heading(title):
    print(f"\n{Fore.LIGHTBLACK_EX}{SEPARATOR}\nRunning: {Fore.CYAN}{title}\n{Fore.LIGHTBLACK_EX}{SEPARATOR}")

def ask(prompt):
    return input(prompt + " (y/n): ").strip().lower() == "y"

def main():
    files = list_programs()
    if not files:
        print(Fore.RED + "No Python files found in the 'Programs/' folder or subfolders.")
        return

    print(Fore.YELLOW + "\nPrograms Available:\n")
    for i, name in enumerate(files, 1):
        print(f"{i}. {name}")

    selected = input(Fore.YELLOW + "\nEnter numbers to run (comma-separated), or press ENTER to run all: ").strip()
    if selected:
        indices = {int(x.strip()) for x in selected.split(",") if x.strip().isdigit()}
        files = [f for i, f in enumerate(files, 1) if i in indices]

    log_enabled = ask("\nSave output to a log file?")
    log_file = None
    if log_enabled:
        name = input("Enter log file name (without .txt): ").strip() or "output"
        log_file = open(f"{name}.txt", "w", encoding="utf-8")

    for relative_path in files:
        abs_path = os.path.join(PROGRAM_FOLDER, relative_path)
        print_heading(relative_path)

        buffer = io.StringIO()
        start = time.time()

        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                code = compile(f.read(), relative_path, 'exec')
                with redirect_stdout(buffer):
                    exec(code, {})
        except Exception:
            buffer.write("Error during execution:\n")
            buffer.write(traceback.format_exc())

        output = buffer.getvalue()
        duration = time.time() - start

        print(output.strip())
        print(f"{Fore.MAGENTA}\nTime taken: {duration:.4f} sec")

        if log_file:
            log_file.write(f"{SEPARATOR}\n{relative_path}\n{SEPARATOR}\n")
            log_file.write(output)
            log_file.write(f"\nTime taken: {duration:.4f} sec\n")

    if log_file:
        log_file.close()
        print(Fore.GREEN + f"\nOutput saved to {name}.txt")

if __name__ == "__main__":
    main()
