# Sudoku Digit Recognition (Computer Vision Project)

## Overview

Command-line tool that recognizes digits from Sudoku board images using classical computer vision. Detects the grid with OpenCV contours, corrects perspective, splits it into 81 cells, and reads digits with Tesseract OCR, printing a formatted 9×9 grid with recognition stats.

---

## Features

- Command-line interface (CLI)
- Automatic detection of the Sudoku grid from an input image
- Perspective normalization and division into 81 cells
- Digit recognition using OCR (Tesseract)
- Clean, formatted Sudoku-style output in the terminal
- Recognition statistics (number of detected digits and empty cells)

---

## Requirements

### System Requirements

- Python **3.8 or higher**
- macOS, Linux, or Windows

### External Dependency

This project uses **Tesseract OCR** for digit recognition.

#### Install Tesseract (macOS)

```bash
brew install tesseract
```

Verify installation:

```bash
tesseract --version
```

---

## Python Dependencies

All required Python packages are listed in `requirements.txt`.

To install them:

```bash
pip install -r requirements.txt
```

Main dependencies include:

- numpy
- opencv-python
- pytesseract
- Pillow

---

## Project Structure

```
sudoku-digit-recognition/
│── main.py
│── requirements.txt
│── README.md
│── image-samples/
│   ├── img1.png
│   └── img2.png
│   └── img3.png
```

---

## How to Run

Activate your virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Run the program with a Sudoku image:

```bash
python3 main.py --image images/img1.png
```

---

## Output

The program prints:

- A formatted **9×9 Sudoku grid** using a standard 3×3 boxed layout
- Empty cells are shown as `.`
- A short statistics summary

### Example Output

```
+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+

Recognized digits: 27/81
Empty cells: 54
```

---

## Methodology (High-Level)

1. **Preprocessing**: Grayscale conversion, noise reduction, and adaptive thresholding
2. **Grid Detection**: Largest contour detection to identify the Sudoku board
3. **Perspective Correction**: Warp the detected grid into a square
4. **Cell Extraction**: Divide the grid into 81 equal cells
5. **Digit Recognition**: Apply OCR to each cell
6. **Output Formatting**: Display results in a readable Sudoku layout with statistics

---

## Limitations

- Recognition accuracy depends on image quality and lighting
- Handwritten or low-contrast digits may reduce OCR accuracy
- The project does not include Sudoku solving logic by design

---

## Notes

- This project strictly follows the requirement of **digit recognition only**
- No machine learning or deep learning models are used
- The focus is on classical computer vision techniques and clean CLI output

