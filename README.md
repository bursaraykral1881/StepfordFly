# DISCONTINUED ⚠️
This project hasn't maintained over a month so its not finished, calibration is wrong. Use at your own risk! 

# Train Game Autopilot 🚂

This project provides a Python-based autopilot script for a train simulator game, leveraging Tesseract OCR and screen capture to read in-game information and automate train controls.

---

## ⚠️ Warning

This script is intended for **educational and experimental purposes only**. Using this script may violate the terms of service of certain games and could lead to penalties including, but not limited to, account suspension or bans. **Use at your own risk.** The developers of this script are not responsible for any consequences arising from its use.

---

## 📂 Project File Structure

Here's the file structure:

    
    StepfordFly
    ├── config.py
    ├── capture.py
    ├── preprocess.py
    ├── ocr_readers.py
    ├── signal_detector.py
    ├── game_controls.py
    └── main.py
    

---

## 🚀 Usage

The script operates by continuously capturing specific regions of your game screen, performing Optical Character Recognition (OCR) on text elements, detecting colors for signal lights, and then executing pre-defined actions (like braking or accelerating) based on the interpreted game state.

To use the autopilot:

1.  **Ensure Game is Running:** The train simulator game must be running and in focus on your primary display (or within a virtual display environment if on a server).

2.  **Calibrate Regions:** Adjust the `REGIONS` dictionary in `train_autopilot.py` to match the exact pixel coordinates of the UI elements in your game. This is critical for accurate OCR and color detection.

3.  **Calibrate Colors:** Fine-tune the `COLOR_RANGES` for your signal lights and the `DOUBLE_YELLOW_THRESHOLD` to accurately detect colors and distinguish between single and double yellow signals.

4.  **Implement Control Actions:** Replace the placeholder `pass` statements in the `Game Control Functions` with actual `pyautogui` or `pynput` commands to simulate key presses or mouse clicks relevant to your game's controls.

5.  **Run the Script:** Execute the `train_autopilot.py` script from your terminal:

    ```python
    python train_autopilot.py
    ```

---

## 🛠️ Installation

### 1. Tesseract OCR Engine

This project relies on the Tesseract OCR engine. You must install it on your system:

* **Windows:** Download the installer from [Tesseract-OCR GitHub Wiki](https://github.com/UB-Mannheim/tesseract/wiki).

* **Linux (Debian/Ubuntu):**
```bash
sudo apt install tesseract-ocr
```

* **macOS (Homebrew):**
```bash
brew install tesseract
```

   If `pytesseract` cannot find Tesseract, you may need to explicitly set `pytesseract.pytesseract.tesseract_cmd` in your script to the full path of the `tesseract.exe` (Windows) or `tesseract` (Linux/macOS) executable.

### 2. Python Dependencies

Install the required Python libraries using pip:

```bash
pip install pytesseract opencv-python numpy Pillow pyautogui
```

### 3. Nix Shell (Recommended for Reproducibility)

For a reproducible development environment, you can use `nix-shell`. Ensure you have Nix installed, then place the provided `shell.nix` file in the project root and run:

```bash
nix-shell
```

This will set up Python with all the necessary libraries and the Tesseract engine.

---

## 📝 TODO

* **Add More Keywords:** Expand the `get_game_status_message()` and `get_dialog_message()` functions to include more relevant in-game status messages and dialogs.

* **Refine Bindings:** Map all necessary in-game controls (e.g., horn, pantograph, specific brake levels) to `pyautogui` or `pynput` actions.

* **Advanced Control Logic:** Implement more sophisticated decision-making based on combinations of sensor inputs (e.g., dynamic braking based on distance and speed, advanced signal interpretation).

* **Error Handling and Robustness:** Enhance error handling for OCR failures and implement fallback mechanisms or retry logic.

* **User Interface (Optional):** Consider adding a simple GUI for calibration and monitoring.

* **Configuration File:** Externalize `REGIONS`, `COLOR_RANGES`, and other parameters into a separate configuration file (e.g., JSON, YAML) for easier management.

---

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).

The Apache License 2.0 is a permissive free software license developed by the Apache Software Foundation. It allows users to use, modify, and distribute the software, even for commercial purposes, under its terms. Key features of this license include:

* Permissiveness: It permits redistribution under the same or a different license, with or without modification.

* Patent Grant: It includes an explicit patent grant from contributors to users, which helps protect users from patent infringement claims related to their use of the software.

* Attribution: It requires that any distributed copies of the software must include the original copyright, patent, trademark, and attribution notices.

* No Warranty: The license explicitly states that the software is provided "as is" without any warranty.

This license is widely used for open-source projects due to its flexibility and the protection it offers to both contributors and users.
