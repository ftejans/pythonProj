import pandas as pd

def check_name_in_excel(file_path, sheet_name, name_column, name_to_check):
    # Load the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Check if the name exists in the specified column
    if name_to_check in df[name_column].values:
        return True
    else:
        return False
    
# Example usage
file_path = 'Attendance.xlsx'
sheet_name = 'wk1'  # Change this to the sheet name you want to read
name_column = 'Name'   # Change this to the column name containing the names
name_to_check = 'Roldan Aquino'

if check_name_in_excel(file_path, sheet_name, name_column, name_to_check.upper()):
    print(f"{name_to_check} is in the list.")
else:
    print(f"{name_to_check} is not in the list.")