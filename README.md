# DISCONTINUED ⚠️
This project hasn't been maintained over a month so its not finished, calibration is wrong. Use at your own risk!

# StepfordFly 🚂

StepfordFly is a Python-based autopilot for the train simulator game "Stepford County Railway", using screen capture and OCR to automate train controls.

## ⚠️ Warning

This script is for **educational purposes only**. Using it may violate the game's terms of service and could lead to penalties. **Use at your own risk.**

## ✨ Features

*   **Automated Speed Control:** Maintains speed based on the current limit.
*   **Signal Detection:** Detects red, green, yellow, and double-yellow signals and reacts accordingly.
*   **Message Handling:** Responds to in-game messages like "Close Doors" and "Depart".
*   **Automatic Braking:** Applies brakes when approaching a station or a red signal.

## 🔧 How It Works

The script continuously performs a loop of the following actions:

1.  **Capture:** Takes screenshots of specific areas of the game screen.
2.  **Preprocess:** Converts the captured images to a format suitable for OCR and color detection.
3.  **Detect & OCR:** Reads text (like speed and distance) using Tesseract OCR and detects signal colors.
4.  **Control:** Sends keyboard commands to the game to control the train based on the gathered information.

## ⚙️ Installation

### 1. Tesseract OCR

You need to install the Tesseract OCR engine.

*   **Windows:** Download from [Tesseract-OCR GitHub Wiki](https://github.com/UB-Mannheim/tesseract/wiki).
*   **Linux (Debian/Ubuntu):** `sudo apt install tesseract-ocr`
*   **macOS (Homebrew):** `brew install tesseract`

### 2. Python Dependencies

Install the required Python libraries:

```bash
pip install pytesseract opencv-python numpy Pillow pyautogui
```

### 3. Nix Shell (Optional)

If you use Nix, you can run `nix-shell` in the project directory to get a shell with all the dependencies.

## 🛠️ Configuration

Before running the script, you need to configure it for your screen setup.

### 1. Screen Regions

The script needs to know where to look on the screen. Use the calibration tool to find the coordinates of the game's UI elements:

```bash
python calibrate.py
```

Move your mouse to the top-left and bottom-right corners of each UI element (like the speedometer) and note the coordinates. Then, update the `REGIONS` dictionary in `config.py` with these values.

### 2. Tesseract Path (if needed)

If `pytesseract` can't find Tesseract, set the `TESSERACT_CMD_PATH` in `config.py` to the location of your Tesseract executable.

### 3. Color Ranges

The script detects signal lights based on HSV color ranges. If the default colors are not detected correctly, you may need to adjust the `COLOR_RANGES` in `config.py`.

## 🚀 Usage

To run the autopilot, navigate to the project's parent directory and run it as a module:

```bash
python3 -m StepfordFly.main
```

Make sure the game is running and is the active window.

## 🔮 Future Improvements

*   More sophisticated control logic (e.g., dynamic braking).
*   A simple GUI for easier configuration.
*   Support for more in-game events and messages.

## 📄 License

This project is licensed under the [GNU Lesser General Public License v3.0](LICENSE).

The LGPL is a free software license that allows developers to use and integrate a software component into their own (even proprietary) software without being required to release the source code of their own components. However, if you modify the licensed component itself, you must release the source code of your modified version.
