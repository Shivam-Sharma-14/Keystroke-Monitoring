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

```bash
pip install pynput pywin32


## Usage

06-07-2025 14:23:11 -> h
06-07-2025 14:23:11 -> e
06-07-2025 14:23:11 -> l
06-07-2025 14:23:11 -> l
06-07-2025 14:23:11 -> o
06-07-2025 14:23:15 -> [CLIPBOARD] pasted@example.com

