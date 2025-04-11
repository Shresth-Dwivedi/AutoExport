CLI Runner Utility
------------------

This tool (`cli_runner.py`) is designed to execute Python scripts located in the 'Programs/' directory, including any subfolders within it.

Key Features:
-------------
- Automatically detects all `.py` files in 'Programs/' and its subdirectories.
- Allows selection of specific files to run by index or runs all by default.
- Optionally logs the output and runtime duration to a text file.
- Clean colored CLI interface using `colorama`.

Usage:
------
1. Place your Python scripts inside the `Programs/` folder or any subdirectory.
2. Run `cli_runner.py`.
3. Select which files to run (by index), or press ENTER to run all.
4. Choose whether to save output to a log file.

Example Folder Structure:
-------------------------
Programs/
├── hello.py
├── math/
│   └── calculator.py
└── games/
    └── snake.py

Requirements:
-------------
- Python 3.7+
- `colorama` (auto-installed if not present)

Logging:
--------
You can save the execution output to a log file. Just provide a name (without extension) when prompted. A `.txt` log will be generated in the current working directory.

Author:
-------
Shresth Dwivedi
