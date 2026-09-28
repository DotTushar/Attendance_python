# Student Attendance & Defaulter Tracker System

A modular Python command-line utility built to log classroom attendance, compute running attendance percentages, and flag students falling below the mandatory 75% attendance threshold.

---

## Why I Built This
Marking attendance by hand on paper sheets consumes valuable lecture time and frequently leads to calculation errors. It also makes it difficult to warn students before they face exam debarment. This utility automates attendance tracking using pure Python data structures, updates records interactively, and highlights at-risk students immediately after every class session.

---

## Features
- Interactive attendance logging via terminal inputs.
- Set difference computation (`All - Present`) to identify absent students instantly without nested loops.
- Automated percentage calculations rounded to two decimal places.
- Dynamic defaulter detection for students below the 75.0% threshold.
- Clean tabular console reports with alignment that adapts to session history length.
- Automated unit tests for calculation and validation logic.

---

## Project Structure
- `data_manager.py`: Stores student records and updates attendance history using set operations.
- `calculator.py`: Pure functions to compute percentages and extract defaulter lists.
- `validator.py`: Sanitizes terminal input by stripping duplicate tokens and invalid roll numbers.
- `report.py`: Formats and displays tabular session summaries and alerts.
- `main.py`: Driver script managing the CLI workflow and user interaction.
- `test_tracker.py`: Automated unit tests built with Python's standard `unittest` module.
- `statement.md`: Problem statement and project scope document.

---

## How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/DotTushar/Attendance_python.git](https://github.com/DotTushar/Attendance_python.git)
   cd Attendance_python