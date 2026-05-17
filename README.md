# Student Grades Analyzer

A beginner-friendly Python data analysis project built using pandas and matplotlib.

This project reads student grade data from a CSV file, analyzes the results, and visualizes grades using a bar chart.

---

## Features

- Load student data from a CSV file
- Calculate:
  - Highest grade
  - Lowest grade
  - Average grade
  - Number of students passed
- Display statistics in the console
- Generate a color-coded bar chart using matplotlib

---

## Technologies Used

- Python
- pandas
- matplotlib

---

## Project Structure

```text
project-folder/
│
├── main.py
├── students.csv
└── README.md
```

---

## Example CSV Format

```csv
Name,Grade
Alice,85
Bob,42
Charlie,76
David,91
```

---

## Installation

Install the required libraries:

```bash
pip install pandas matplotlib
```

---

## How to Run

Run the Python file:

```bash
python main.py
```

The program will:
1. Load the CSV file
2. Analyze student grades
3. Print statistics
4. Display a graph

---

## Example Output

```text
The highest grade is: 91
The lowest grade is: 42
The average grade is: 73.5
The number of students passed is: 3
```

---

## Graph Features

- Green bars = grades above average
- Red bars = grades below average
- Dashed line = class average

---

## Future Improvements

- Add better error handling
- Export reports to text files
- Add support for multiple subjects
- Add GUI support using Tkinter
- Save graphs as image files

---

## Author

Made by Syed Asadulla Hussaini

---

## License

This project is open-source and free to use.

---

## About

This project was created to practice Python data analysis fundamentals using pandas 
and data visualization using matplotlib. It demonstrates file handling, dataframe 
analysis, plotting graphs, and writing clean modular Python code. An important feature 
is the program doesnt crash if the csv file has missing columns or columns labeled 
dfferently than ("Name", "Grade").
