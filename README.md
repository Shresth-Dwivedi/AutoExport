# 🚀 AutoExport

AutoExport is a Python-based GUI application that helps you export your programming assignments (Python, C++, Java, etc.) into a neatly formatted Word `.docx` document — complete with code, outputs, and visuals. It’s designed for students and developers who want to generate clean submission-ready documents with just a few clicks.

---

## 🎯 Features

- ✅ CustomTkinter-based modern GUI
- 📄 Exports code from multiple languages into `.docx`
- 🖼️ Embeds execution output and generated visuals (currently only Python and matplotlib supported for output generation)
- 📝 Adds instructor, course, semester metadata
- 📁 Auto-select files and customize export folder
- 🔍 Optional CLI runner for batch testing

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

**Minimum requirements:**

```
customtkinter
pillow
python-docx
matplotlib
```

---

## 🚀 How to Run

### GUI App:

```bash
python autoexport.py
```

### CLI Tool (optional):

### `tools/cli_runner.py`

A command-line interface utility that executes selected `.py` files from the `Programs/` directory **and its subfolders**.

- Displays a list of available programs with indexed selection.
- Supports optional logging of output and time taken.
- Automatically installs `colorama` if missing.
(More language support in new versions soon!)

---

## 📁 Project Structure

```
AutoExport/
│
├── autoexport.py              # Main GUI application for exporting assignments
├── LICENSE                    # MIT License information
├── README.md                  # Main README with usage and setup instructions
├── requirements.txt           # Python dependencies for the project
│
├── icons/                     # Contains icons used in the GUI
│   └── (multiple icon files...)
│
├── tools/                     # Additional tools and command-line utilities
│   ├── cli_runner.py          # CLI tool to run programs and collect outputs
│   ├── README.txt             # Info and usage for cli_runner.py
│   └── Programs/              # Sample/test Python programs for CLI testing
│
└── ...

```

---

## ❤️ Support

If this tool helped you, consider supporting the creator 🙏

**UPI ID:** `shresthdwivedi03@axl`

You can also connect:

- [GitHub](https://github.com/Shresth-Dwivedi)
- [LinkedIn](https://linkedin.com/in/shresth-dwivedi)
- [X](https://x.com/theDavyDee)

---

## 🎨 Icon Credits

This project uses custom and original icons sourced from the following platforms:

- [Flaticon](https://www.flaticon.com/)
- [Freeicons.io](https://freeicons.io/)

Some icons have been modified (e.g., resized, recolored) to better match the app's UI.

These icons are used under their respective free-use licenses, such as the [Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), which allows adaptation with attribution.

> If you're a creator and see your icon used here, feel free to contact me for additional credit or changes.


## 📄 License

MIT License.  
You are free to use, modify, and distribute this tool. Just give credit where it’s due 🙂

---

## ⬇️ Download

You can download the latest version of AutoExport here:

👉 [Download .exe from the latest release](https://github.com/Shresth-Dwivedi/AutoExport/releases/latest)

> No installation required. Just download and double-click `autoexport-v1.0.exe`.


## ✨ Author

Made with ❤️ and ☕ by **Shresth Dwivedi**
