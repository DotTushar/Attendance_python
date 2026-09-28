# Problem Statement: Student Attendance & Defaulter Tracker System

## 1. Background & Context
At VIT Bhopal University, maintaining a minimum of 75% classroom attendance is mandatory to appear in end-semester examinations Falling below this threshold results in debarment from exams Manual recording and tracking of student attendance across 25+ lecture sessions is tedious, time-consuming, and prone to human calculation errors

## 2. Problem Description
Traditional manual attendance handling suffers from three primary issues
1. **Instructional Time Loss:** Calling out roll numbers consumes valuable lecture minutes every class
2. **Human Calculation Errors:** Manually computing attendance percentages across numerous sessions leads to mistakes, incorrectly classifying students above or below the 75% cutoff
3. **Delayed Visibility:** Students often realize they have attendance shortages only after official debarment lists are published, leaving no time for academic recovery

## 3. Project Objective
To develop a modular, pure Python 3 command-line utility that uses fundamental data structures (dictionaries, lists, sets) to
- Record interactive daily session attendance using roll numbers
- Automatically detect absentees using set difference operations (`All - Present`)
- Compute exact running attendance percentages per student rounded to two decimal places
- Instantly identify and flag defaulters falling below the 75.0% threshold
- Provide clean tabular summaries and alerts after each session

## 4. Scope & Constraints
- Implemented strictly using standard Python 3 (no third-party dependencies or external libraries)
- Decomposed into 6 distinct modules to ensure high maintainability and testability
- Includes automated unit tests verifying arithmetic and validation logic