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

   