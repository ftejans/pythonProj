import pandas as pd
import os
import re
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def extract_header_info(file_path):
    with open(file_path, 'r') as file:
        package_name = file.readline().strip().split(': ')[1]
        duration = int(file.readline().strip().split(': ')[1])
        interval = int(file.readline().strip().split(': ')[1])

    return package_name, duration, interval

def extract_cpu_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    cpu_data = []
    for line in lines:
        match = re.search(r'%Cpu\(s\):\s+([\d.]+)\s+us,\s+([\d.]+)\s+sy,\s+([\d.]+)\s+ni,\s+([\d.]+)\s+id,\s+([\d.]+)\s+wa,\s+([\d.]+)\s+hi,\s+([\d.]+)\s+si,\s+([\d.]+)\s+st', line)
        if match:
            cpu_data.append([float(match.group(i)) for i in range(1, 9)])
    
    return cpu_data

def save_to_excel(package_name, duration, interval, cpu_data, template_file, output_file):
    df = pd.DataFrame(cpu_data, columns=['user', 'sys', 'nice', 'idle', 'wa', 'hi', 'si', 'st'])
    
    df['cpu_consumption'] = (df['user'].astype(float) + df['nice'].astype(float) + df['sys'].astype(float))
    
    max_cpu_consumption = round(df['cpu_consumption'].max()/4, 2)
    min_cpu_consumption = round(df['cpu_consumption'].min()/4, 2)
    avg_cpu_consumption = round(df['cpu_consumption'].mean()/4, 2)

    workbook = load_workbook(template_file)
    workbook.save(output_file)
    sheet = workbook['Measurements']

    for row in dataframe_to_rows(df, index=False, header=False):
        sheet.append(row)

    sheet = workbook['CPU Consumption']
    sheet['C3'] = package_name
    sheet['C4'] = duration
    sheet['C5'] = interval
    sheet['C45'] = max_cpu_consumption  
    sheet['C46'] = min_cpu_consumption  
    sheet['C47'] = avg_cpu_consumption
    
    workbook.save(output_file)
    print()
    print(f"Data appended successfully to {output_file}")

if __name__ == '__main__':
    input_file = 'cpu_measurement_subcore_results.txt'
    template_file = 'CPU_Measurement_Results_SubCore_Template.xlsx'
    output_file = 'CPU_Measurement_Results_SubCore.xlsx'
    
    # Extract CPU measurements from the input file
    package_name, duration, interval = extract_header_info(input_file)
    cpu_data = extract_cpu_data(input_file)
    
    # Save the CPU measurements to the Excel file
    save_to_excel(package_name, duration, interval, cpu_data, template_file, output_file)
    
    print("Update successful")
