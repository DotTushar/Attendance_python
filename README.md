# Student Attendance & Defaulter Tracker System

A console-based Python project to log daily classroom attendance, calculate percentages per student, and immediately flag anyone falling below the college's mandatory 75% cutoff[cite: 9].

---

## Why I Built This
Marking attendance by hand on paper sheets usually takes too long and leads to counting mistakes. It also makes it hard to warn students before they get debarred for low attendance. I built this program to keep attendance history in simple data structures, calculate percentages automatically, and show an updated defaulter list after each class[cite: 9].

---

## Features
- Interactive attendance marking by typing present roll numbers in the terminal[cite: 9].
- Uses Python set difference (`All - Present`) to quickly find who is absent without nested loops.
- Computes each student's attendance percentage to two decimal places.
- Automatically flags anyone with less than 75% attendance as a "Defaulter".
- Separated into three separate files to keep the code organized[cite: 8, 9].

---

## Project Structure
- `data_manager.py`: Stores the initial student attendance dictionary and handles the set logic to log today's session[cite: 8].
- `calculator.py`: Contains functions to calculate attendance percentage and filter defaulters below 75%[cite: 8].
- `report.py`: Prints the formatted table and warning messages to the terminal[cite: 8].
- `main.py`: The entry script that runs the program, asks for input, and updates records[cite: 8].

---

## Technologies Used
- Python 3[cite: 9]
- Built-in data structures: Dictionaries, Lists, and Sets[cite: 8, 9]
- No external packages required (runs using standard Python)[cite: 10]

---

## How to Run

1. Clone this repository[cite: 8, 10]:
   ```bash
   git clone [https://github.com/DotTushar/Attendance_python.git](https://github.com/DotTushar/Attendance_python.git)
   cd Attendance_python

```

2. Run the main file:


```bash
python main.py

```


3. Type the roll numbers present in class (separated by a space, e.g., `101 103`) and press Enter.



---

## Sample Run

```text
Starting Attendance & Defaulter Tracker System...

================ ATTENDANCE SUMMARY ================
Roll No         Records                 Percentage      Status
----------------------------------------------------
101             [1, 1, 1, 0, 1]         80.0%           Eligible
102             [1, 0, 0, 1, 0]         40.0%           Defaulter
103             [1, 1, 1, 1, 1]         100.0%          Eligible
104             [0, 0, 1, 0, 0]         20.0%           Defaulter

Total Defaulters (< 75%): 2
Warning: Roll No 102 has only 40.0% attendance!
Warning: Roll No 104 has only 20.0% attendance!
====================================================

Enter roll numbers present today (separated by space, e.g. 101 103):
> 101 103

Attendance logged successfully.
Students absent today: {'102', '104'}

Updated Report Post-Session:

================ ATTENDANCE SUMMARY ================
Roll No         Records                 Percentage      Status
----------------------------------------------------
101             [1, 1, 1, 0, 1, 1]      83.33%          Eligible
102             [1, 0, 0, 1, 0, 0]      33.33%          Defaulter
103             [1, 1, 1, 1, 1, 1]      100.0%          Eligible
104             [0, 0, 1, 0, 0, 0]      16.67%          Defaulter
====================================================

```