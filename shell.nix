{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    tesseract
    python313Packages.pytesseract
    python313Packages.opencv4
    python313Packages.numpy
    python313Packages.pillow
    python313Packages.pyautogui
  ];

  shellHook = ''
  python3 main.py
  '';
}
