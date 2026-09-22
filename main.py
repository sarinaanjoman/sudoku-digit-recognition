import cv2
import pytesseract
import argparse

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    return thresh

def find_sudoku_grid(image):
    # Find contours in the image
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assume the largest contour is the Sudoku grid
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Get the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    # Crop the image to the bounding box
    cropped = image[y:y+h, x:x+w]
    
    return cropped, (x, y, w, h)


def extract_cells(image):
    cells = []
    cell_size = image.shape[0] // 9
    
    for i in range(9):
        for j in range(9):
            # Extract each cell
            cell = image[i*cell_size:(i+1)*cell_size, j*cell_size:(j+1)*cell_size]
            
            # Assuming `cell` is the extracted cell image
            margin = 5  

            # Crop the cell from all four sides
            cell_cropped = cell[margin:-margin, margin:-margin]
            # Clean up the cell image
            cell_cropped = cv2.resize(cell_cropped, (28, 28))
            cell_cropped = cv2.bitwise_not(cell_cropped)
            
            cells.append(cell_cropped)
    
    return cells

def recognize_numbers(cells):
    sudoku_grid = []
    
    for cell in cells:
        # Use Tesseract to recognize the number in the cell
        text = pytesseract.image_to_string(cell, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        
        # If Tesseract recognizes a number, add it to the grid
        if text.strip():
            sudoku_grid.append(int(text.strip()))
        else:
            sudoku_grid.append(0)
    
    return sudoku_grid

def print_sudoku_grid(grid, empty_char="."):
    """Print Sudoku grid in a classic 3x3 boxed format. grid is a flat list of 81 ints."""
    print("\nSudoku Grid:\n")

    def cell(v):
        v = int(v)
        return empty_char if v == 0 else str(v)

    line = "+-------+-------+-------+"
    for r in range(9):
        if r % 3 == 0:
            print(line)

        row = grid[r*9:(r+1)*9]
        a = " ".join(cell(x) for x in row[0:3])
        b = " ".join(cell(x) for x in row[3:6])
        c = " ".join(cell(x) for x in row[6:9])
        print(f"| {a} | {b} | {c} |")

    print(line)


def main(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Find the Sudoku grid
    sudoku_grid_image, _ = find_sudoku_grid(preprocessed_image)
    
    # Extract cells from the grid
    cells = extract_cells(sudoku_grid_image)
    
    # Recognize numbers in each cell
    sudoku_grid = recognize_numbers(cells)
    # Display the recognized numbers
    print_sudoku_grid(sudoku_grid)

    recognized = sum(1 for v in sudoku_grid if int(v) != 0)
    empty = 81 - recognized
    print(f"\nRecognized digits: {recognized}/81")
    print(f"Empty cells: {empty}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sudoku digits recognition")
    parser.add_argument("--image", type=str, required=True, help="Path to input image")
    args = parser.parse_args()
    main(args.image)        