# Student Attendance & Defaulter Tracker System

A modular Python-based management utility designed to record daily class attendance, calculate percentage metrics, and flag academic defaulters below the mandatory 75% threshold.

---

## 📌 Project Overview
Monitoring student attendance manually often leads to clerical errors and delayed notifications for at-risk students. This project provides a terminal-driven solution to track attendance dynamically across sessions without needing heavy external database dependencies.

---

## 🚀 Key Features
* **Modular Architecture**: Divided into distinct functions for marking attendance, percentage calculation, defaulter filtering, and reporting.
* **Attendance Ledger**: Uses Python Dictionaries to map student identifiers to session attendance lists.
* **Absentee Detection**: Uses Python Sets and the set difference (`-`) operation to instantly isolate absentees based on daily roll entries.
* **Defaulter Alerts**: Automatically identifies students below the 75% attendance threshold with warning summaries.

---

## 🛠️ Data Structures Implemented
* **Dictionary (`dict`)**: Stores student records mapping Roll Numbers to their attendance history.
* **List (`list`)**: Tracks sequential binary attendance values (`1` for Present, `0` for Absent).
* **Set (`set`)**: Manages the registered student pool and calculates daily absentees via set operations.

---

## 💻 How to Run the Program

### Prerequisites
* Python 3.8 or higher installed on your system.

### Execution
1. Clone the repository:
   ```bash
git clone https://github.com/DotTushar/Attendance_python.git
cd Attendance_python
