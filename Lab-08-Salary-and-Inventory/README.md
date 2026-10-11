# Lab 8: Salary Calculation and Inventory Management in Calc

## Part A — Salary calculation

### Aim
To calculate gross salary and net salary using spreadsheet formulas.

### Procedure
1. Open `Salary_Sheet.csv` in Calc.
2. Gross Salary (F2): `=C2+D2`
3. Net Salary (G2): `=F2-E2`
4. Fill formulas down, apply currency formatting, and save as `Salary_Sheet.ods`.

### Expected Output
Gross salary equals basic salary plus allowances. Net salary equals gross salary minus deductions.

### Conclusion
A salary sheet was prepared using arithmetic formulas.

## Part B — Inventory management

### Aim
To calculate stock value and flag items that have reached a low-stock level.

### Procedure
1. Open `Inventory_Register.csv` in Calc.
2. Stock Value (E2): `=C2*D2`
3. Status (G2): `=IF(C2<F2;"REORDER";"OK")`. If your locale uses commas, use `=IF(C2<F2,"REORDER","OK")`.
4. Fill formulas down and save as `Inventory_Register.ods`.

### Expected Output
Stock value is calculated as quantity multiplied by unit price. The status shows `REORDER` when quantity is below the reorder level; otherwise it shows `OK`.

### Conclusion
Salary calculations and basic inventory tracking were completed using Calc.
