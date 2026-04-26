# NVIDIA GPU Monitor
// In English: NVIDIA GPU Monitor
A simple terminal-based GUI to monitor NVIDIA GPU usage, memory, and temperature using the `nvidia-smi` command.

## Features
- Displays GPU name, memory usage, GPU utilization, and temperature.
- Updates every second for real-time monitoring.
- Uses the `rich` library for a visually appealing terminal interface.

## Installation
1. Ensure you have Python 3 installed.
2. Install the required library, using requirements.txt:
    ```
    pip install -r requirements.txt
    ```
## Usage
Run the script:
```
python nvidia_smi_gui.py
```
This will open a terminal-based GUI that updates every second with the latest GPU information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.