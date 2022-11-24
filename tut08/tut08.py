import re
from datetime import datetime
start_time = datetime.now()

#Help
def scorecard():
	#A dictionary having name of each player and short name used in commmentary
	name = {'Bhuvneshwar':'Bhuvneshwar Kumar','Rahul':'KL Rahul', 'Rizwan':'Mohammad Rizwan(w)', 'Babar Azam':'Babar Azam(c)', 'Arshdeep Singh':'Arshdeep Singh', 'Fakhar Zaman':'Fakhar Zaman', 'Hardik Pandya':'Hardik Pandya', 'Avesh Khan':'Avesh Khan', 'Iftikhar Ahmed':'Iftikhar Ahmed', 'Chahal':'Yuzvendra Chahal', 'Jadeja':'Ravindra Jadeja', 'Khushdil':'Khushdil Shah', 'Shadab Khan':'Shadab Khan', 'Asif Ali':'Asif Ali', 'Mohammad Nawaz':'Mohammad Nawaz', 'Haris Rauf':'Haris Rauf', 'Naseem Shah':'Naseem Shah', 'Dahani':'Shahnawaz Dahani', 'Rohit':'Rohit Sharma(c)', 'Kohli':'Virat Kohli', 'Suryakumar Yadav':' Suryakumar Yadav', 'Karthik':'Dinesh Karthik(w)'}
	#List of names of players of Team India
	TeamIndia =[ 'Rohit','Rahul' ,'Kohli','Suryakumar Yadav', 'Karthik', 'Hardik Pandya', 'Jadeja', 'Bhuvneshwar', 'Avesh Khan', 'Chahal', 'Arshdeep Singh']
	TeamPak = ['Babar Azam', 'Rizwan', 'Fakhar Zaman', 'Iftikhar Ahmed', 'Khushdil', 'Asif Ali', 'Shadab Khan', 'Mohammad Nawaz', 'Naseem Shah', 'Haris Rauf', 'Dahani']
	#Opening the file
	f = open('Scorecard.txt', 'w')
	#Reading the innings file
	f1 = open('pak_inns1.txt', 'r')
	f2 = open('india_inns2.txt', 'r')

	#Reading all the lines
	Pak = f1.readlines()
	Ind = f2.readlines()