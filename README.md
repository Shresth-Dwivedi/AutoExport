# 🚀 AutoExport

AutoExport is a sleek, modern GUI tool for Windows that lets you batch export your programming assignments into a clean, formatted Word document. It automatically executes your code, captures outputs (including plots from `matplotlib`), and supports multiple languages like Python, Java, C++, C, JavaScript, Go, Ruby, PHP and C#.

---

## 🎯 Features

- ✅ CustomTkinter-based modern GUI
- 🧠 Smart language detection (Python, Java, C, C++, JavaScript, Go, and more)
- ⚙️ Auto-compilation and execution of code files
- 📦 Supports user input detection during execution
- 📸 Visual output capturing via `matplotlib`
- 📄 Generates professional `.docx` reports with:
  - User metadata
  - Code blocks
  - Outputs
  - Auto-added visual results
- 🔍 Built-in file browser with sorting, searching, and filtering

---

## 🛠 Requirements

### For `.exe` version (Windows 64-bit installer)

- Operating System: Windows XP or older (64-bit)
- Language Runtimes/Compilers: Ensure the necessary compilers or interpreters for the supported programming languages are installed and properly added to your system's PATH environment variable.

>⚠️ AutoExport relies on your system's installed compilers or interpreters to build and execute code of the language you wish to export to the document. Without these language runtimes, the application will not generate outputs.

You can export programs of the following languages:

        Supported Languages: Python, Java, C++, C, C#, Go, JavaScript, Ruby, PHP

>⚠️ You only need the runtime tools for the language(s) you wish to use the application with. 
>
> If you wish to use the application **only for `.py` programs**, you may ignore these instructions.

### Installation

Download the latest Windows installer `autoexport-2.3-windows-setup-x64.exe` from the [Releases](https://github.com/Shresth-Dwivedi/AutoExport/releases) page and run the setup.

>⚠️ This is specifically for 64-bit systems, running Windows XP or older.

---

### For `.py` version (manual run via Python)

- Operating System: Windows XP or older
- Python 3.10 or higher (Recommended: Python 3.12+)
- Clone the repository:
  ```bash
  git clone https://github.com/Shresth-Dwivedi/AutoExport.git
  cd AutoExport

#### Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```
Your ***requirements.txt*** should include:
```
customtkinter
pillow
python-docx
matplotlib
cairosvg
```
#### Additional tools (based on language):

**Language Runtimes/Compilers:** Ensure the necessary compilers or interpreters for the supported programming languages are installed and properly added to your system's PATH environment variable.


## 📁 Project Structure

```
AutoExport/
├── assets/ 
│ ├── buddy/ 
│ ├── icons/ 
│ └── themes/
├── .gitignore 
├── autoexport.py 
├── LICENSE 
├── README.md 
├── requirements.txt 
└── version.txt 

```

---

## ❤️ Support

If this application helped you, consider donating 🙏

**UPI ID:** `shresthdwivedi03@axl`

You can also connect through social media:

- [LinkedIn](https://linkedin.com/in/shresth-dwivedi)
- [X](https://x.com/theDavyDee)
- [BlueSky](https://bsky.app/profile/shresthdwivedi.bsky.social)

---

## 🎨 Icon Credits

This project uses custom and original icons sourced from [Apple SF Regular Filled](https://icons8.com/icons/sf-regular-filled) icon pack from [Icons8](https://icons8.com/).

Some icons have been modified (e.g., resized, recolored) to better match the app's UI.

These icons are used under the [**Universal Multimedia Licensing Agreement (UMLA)**]((https://icons8.com/vue-static/landings/pricing/icons8-license.pdf#:~:text=Universal%20Multimedia%20Licensing%20Agreement%20(%22Agreement%22%2C%20or%20%22License%22):,and%20content%20with%20certain%20provisions%20or%20restrictions.&text=If%20a%20Licensee%20or%20User%20shall%20have,any%20time%2C%20an%20%22Enterprise%22%20License%20is%20required.)) for Icons8, which allows adaptation with attribution.

> If you're a creator and see your icon used here, feel free to contact me for additional credit or changes.


## 📄 License

**AutoExport License v2.3 – Non-Commercial, No-Derivatives**

This software is licensed for **personal and educational use only**. You are permitted to use, copy, and share the software as-is, provided that proper credit is given. **Commercial use, redistribution for profit, modification, reverse engineering, or creation of derivative works is strictly prohibited.** All distributed copies must retain the original license and author attribution.

>For full details, please refer to the [LICENSE](https://github.com/Shresth-Dwivedi/AutoExport/blob/main/LICENSE) file in the repository (also included in the installed version of the application).

For questions, contributions, or feedback, contact: shresthdwivedi@yahoo.com


---

## ✨ Author

Made with ❤️ and ☕ by [**Shresth Dwivedi**](https://github.com/Shresth-Dwivedi)
