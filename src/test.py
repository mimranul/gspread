import gspread

gc = gspread.service_account(filename="C:\\Users\\rowsh\\Downloads\\pythonspreadsheet-304613-097ebc49384e.json")

project_aam = gc.open("Project Aam")
delivery_sheet = project_aam.worksheet("Delivery Sheet")

# print(project_aam.sheet1.get('A1'))
print("Rows: ", delivery_sheet.row_count)
print("Cols: ", delivery_sheet.col_count)
print("")
