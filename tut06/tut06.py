from platform import python_version
import csv

import pandas as pd

from datetime import datetime
import openpyxl
start_time = datetime.now()


def attendance_report():
    try:
        inp_file = pd.read_csv('input_attendance.csv')
        inp = inp_file.fillna("2001CCXX Random")
    except:
        print("File not found")

    try:
        rollno_inp = pd.read_csv('input_registered_students.csv')
    except:
        print('File containing name of all students is missing!')

    # mr = sheet_input.max_row

    mc = sum(1 for row in open("input_registered_students.csv"))
    mc_consolidated = sum(1 for row in open("input_attendance.csv"))
    total_dates = list()
    for j in range(0, mc_consolidated-1):
        day = inp.at[j, 'Timestamp'].split()[0].split('-')[0]
        month = inp.at[j, 'Timestamp'].split()[0].split('-')[1]
        year = inp.at[j, 'Timestamp'].split()[0].split('-')[2]
        date = datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d").date()
        day_name = date.strftime("%A")
        if day_name == "Monday" or day_name == "Thursday":
            if inp.at[j, 'Timestamp'].split()[0] not in total_dates:
                total_dates.append(inp.at[j, 'Timestamp'].split()[0])
    # max_att=0
    # max_roll=""
    fileName_consolidated = ".\output\\attendance_report_consolidated.xlsx"

   