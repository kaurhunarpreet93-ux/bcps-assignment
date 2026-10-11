# Lab 7: Attendance Spreadsheet in Calc

## Aim
To calculate students' attendance percentages and identify attendance below a selected threshold.

## Procedure
1. Open `Attendance_Record.csv` in Calc.
2. Review classes held and classes attended.
3. In E2, enter `=IF(C2=0;0;D2/C2)` and format the cell as Percentage. If your locale uses commas, use `=IF(C2=0,0,D2/C2)`.
4. Fill the formula down the column.
5. Optionally use conditional formatting to highlight attendance below 75%.
6. Save as `Attendance_Record.ods`.

## Expected Output
The Attendance Percentage column shows the fraction of classes attended as a percentage. For example, 36 attended out of 45 held equals 80%.

## Conclusion
An attendance register was prepared and attendance percentage was calculated using a formula.
