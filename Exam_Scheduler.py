import datetime 
from datetime import timedelta

college_name = 'Bhaktapur Multiple Campus'

start_date = '2025-05-01'
exams = ['Python Programming',0,'Data Structure',3,'Database Systems',6,'Computer Network',10,
         'Mathematics',14]

def parse_date(date_str):
    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:]
    date = datetime.date(int(year),int(month),int(day))
    return date

def get_exam_date(start_str,days):
    date = parse_date(start_date)
    new_date = date + timedelta(days)
    return date, str(new_date)

def print_schedule(start_str,exams):
    print(f'Schedule for {college_name} exams')
    for i in range(0,len(exams),2):
        start_date,date = get_exam_date(start_str,exams[i+1])

        subject = exams[i]
        print(f'{subject} : {date}')

print_schedule(start_date,exams)


