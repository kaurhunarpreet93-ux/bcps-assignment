# Lab 6: Student Marksheet in LibreOffice Calc

## Aim
To prepare a student marksheet and calculate total, average, maximum, and minimum marks using Calc functions.

## Procedure
1. Open `Student_Marksheet.csv` in LibreOffice Calc.
2. Check the columns: Roll No., Name, three subject marks, Total, and Average.
3. Enter the formulas shown below in row 2 if the formula columns are blank.
4. Fill or copy the formulas down for each student.
5. Use MAX and MIN on the marks range to find the highest and lowest marks.
6. Save as `Student_Marksheet.ods`.

## Formulas
Assuming subject marks are in C2:E2:
- Total in F2: `=SUM(C2:E2)`
- Average in G2: `=AVERAGE(C2:E2)`
- Highest subject mark for a student: `=MAX(C2:E2)`
- Lowest subject mark for a student: `=MIN(C2:E2)`
- Highest mark in the full marks range: `=MAX(C2:E6)`
- Lowest mark in the full marks range: `=MIN(C2:E6)`

## Expected Output
Totals and averages are calculated for each student. MAX and MIN return the highest and lowest values in the selected ranges.

## Conclusion
A student marksheet was created and spreadsheet functions were used to perform calculations.
