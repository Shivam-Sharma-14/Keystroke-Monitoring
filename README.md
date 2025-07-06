# Keystroke-Monitoring Tool
A simple and lightweight keystroke monitoring tool built with Python. It captures keypresses in real-time, and saves everything with timestamps in a .log file. Designed for testing, input behavior analysis, and personal learning — built with minimal dependencies and a focus on clarity.


## Features

- Logs all keypresses with timestamps
- Detects special keys like Enter, Tab, Backspace, etc.
- Writes data to a readable `.log` file (`activity.log`)
- Silent `.exe` build using PyInstaller (`-w -F`)
- Clean output formatting
- Designed to be small and simple

## Usage

1. Clone the repository
2. Install dependencies:

## bash
pip install pynput pywin32


## Output

06-07-2025 14:23:11 -> h
06-07-2025 14:23:11 -> e
06-07-2025 14:23:11 -> l
06-07-2025 14:23:11 -> l
06-07-2025 14:23:11 -> o


## Alternative

- Make a separate file with Keystroke
- Copy the code into VSCode with a file name Keystroke_Monitoring.py
- Now on the address bar of a file Keystroke search for "powershell"
- Now paste this "python -m PyInstaller -w -F Keystroke_Monitoring.py" to convert the python code into executable file (.exe)
- Boom all done...You will get a "dist" folder inside "Keystroke" file, there will a file name with .exe file.
- Click on that file to run...it will get started and will capture all the Keystroke.
- All the keystroke will be saved in a file name "action.log" change the extension into "action.txt" to get into readable format
- Boom....Here You Are Done.


