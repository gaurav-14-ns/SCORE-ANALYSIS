import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#USER INPUTS
def year_1():
    try:
        num_stu_1st = int(input('Enter number of students in 1st year - '))
        stu_score = []
        for i in range(num_stu_1st):
            name = input(f'Name {i + 1} - ').title()
            score = int(input(f'Total Score {i + 1} - '))
            stu_score.append({'NAME': name, 'SCORE': score})

        # dataframe creation
        year1 = pd.DataFrame(stu_score)

        #if file exists(to avoid column heading repetition)
        #saving to csv
        if os.path.exists(r"C:\Users\Gaurav\Downloads\year_1.csv"):
            y1 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_1.csv") # read the file
            last_slno = y1['SL.NO.'].max() # get the last serial number
            start_slno = last_slno + 1 # make the new starting serial number as - previous + 1
            year1['SL.NO.'] = range(start_slno,start_slno+len(year1))  # serial number column adding - range(start,end+1)
            year1 = year1[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year1.to_csv(r"C:\Users\Gaurav\Downloads\year_1.csv", index=False,header=False, mode='a')
            # saved confirmation
            print('FILE SAVED!')
        else:
            year1['SL.NO.'] = range(1, len(year1) + 1)  # serial number column adding
            year1 = year1[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year1.to_csv(r"C:\Users\Gaurav\Downloads\year_1.csv", index=False, mode='w')
            # saved confirmation
            print('FILE SAVED!')

    except Exception as e:
        print(f'Error!\n{str(e)}')

def year_2():
    try:
        num_stu_2nd = int(input('Enter number of students in 2nd year - '))
        stu_score = []
        for i in range(num_stu_2nd):
            name = input(f'Name {i + 1} - ').title()
            score = int(input(f'Total Score {i + 1} - '))
            stu_score.append({'NAME': name, 'SCORE': score})

        # dataframe creation
        year2 = pd.DataFrame(stu_score)

        #if file exists(to avoid column heading repetition)
        #saving to csv
        if os.path.exists(r"C:\Users\Gaurav\Downloads\year_2.csv"):
            y2 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_2.csv") # read the file
            last_slno = y2['SL.NO.'].max() # get the last serial number
            start_slno = last_slno + 1 # make the new starting serial number as - previous + 1
            year2['SL.NO.'] = range(start_slno,start_slno+len(year2))  # serial number column adding - range(start,end+1)
            year2 = year2[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year2.to_csv(r"C:\Users\Gaurav\Downloads\year_2.csv", index=False,header=False, mode='a')
            # saved confirmation
            print('FILE SAVED!')
        else:
            year2['SL.NO.'] = range(1, len(year2) + 1)  # serial number column adding
            year2 = year2[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year2.to_csv(r"C:\Users\Gaurav\Downloads\year_2.csv", index=False, mode='w')
            # saved confirmation
            print('FILE SAVED!')

    except Exception as e:
        print(f'Error!\n{str(e)}')

def year_3():
    try:
        num_stu_3rd = int(input('Enter number of students in 3rd year - '))
        stu_score = []
        for i in range(num_stu_3rd):
            name = input(f'Name {i + 1} - ').title()
            score = int(input(f'Total Score {i + 1} - '))
            stu_score.append({'NAME': name, 'SCORE': score})

        # dataframe creation
        year3 = pd.DataFrame(stu_score)

        #if file exists(to avoid column heading repetition)
        #saving to csv
        if os.path.exists(r"C:\Users\Gaurav\Downloads\year_3.csv"):
            y3 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_3.csv") # read the file
            last_slno = y3['SL.NO.'].max() # get the last serial number
            start_slno = last_slno + 1 # make the new starting serial number as - previous + 1
            year3['SL.NO.'] = range(start_slno,start_slno+len(year3))  # serial number column adding - range(start,end+1)
            year3 = year3[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year3.to_csv(r"C:\Users\Gaurav\Downloads\year_3.csv", index=False,header=False, mode='a')
            # saved confirmation
            print('FILE SAVED!')
        else:
            year3['SL.NO.'] = range(1, len(year3) + 1)  # serial number column adding
            year3 = year3[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year3.to_csv(r"C:\Users\Gaurav\Downloads\year_3.csv", index=False, mode='w')
            # saved confirmation
            print('FILE SAVED!')

    except Exception as e:
        print(f'Error!\n{str(e)}')

def year_4():
    try:
        num_stu_4th = int(input('Enter number of students in 4th year - '))
        stu_score = []
        for i in range(num_stu_4th):
            name = input(f'Name {i + 1} - ').title()
            score = int(input(f'Total Score {i + 1} - '))
            stu_score.append({'NAME': name, 'SCORE': score})

        # dataframe creation
        year4 = pd.DataFrame(stu_score)

        #if file exists(to avoid column heading repetition)
        #saving to csv
        if os.path.exists(r"C:\Users\Gaurav\Downloads\year_4.csv"):
            y4 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_4.csv") # read the file
            last_slno = y4['SL.NO.'].max() # get the last serial number
            start_slno = last_slno + 1 # make the new starting serial number as - previous + 1
            year4['SL.NO.'] = range(start_slno,start_slno+len(year4))  # serial number column adding - range(start,end+1)
            year4 = year4[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year4.to_csv(r"C:\Users\Gaurav\Downloads\year_4.csv", index=False,header=False, mode='a')
            # saved confirmation
            print('FILE SAVED!')
        else:
            year4['SL.NO.'] = range(1, len(year4) + 1)  # serial number column adding
            year4 = year4[['SL.NO.', 'NAME', 'SCORE']]  # reordering columns
            year4.to_csv(r"C:\Users\Gaurav\Downloads\year_4.csv", index=False, mode='w')
            # saved confirmation
            print('FILE SAVED!')

    except Exception as e:
        print(f'Error!\n{str(e)}')

def representation():
    try:
        # files
        y1 = r"C:\Users\Gaurav\Downloads\year_1.csv"
        y2 = r"C:\Users\Gaurav\Downloads\year_2.csv"
        y3 = r"C:\Users\Gaurav\Downloads\year_3.csv"
        y4 = r"C:\Users\Gaurav\Downloads\year_4.csv"

        if all(os.path.exists(i) for i in [y1, y2, y3, y4]):
            # reading csv files
            year1 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_1.csv")
            year2 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_2.csv")
            year3 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_3.csv")
            year4 = pd.read_csv(r"C:\Users\Gaurav\Downloads\year_4.csv")

            # x-axis
            years = [1, 2, 3, 4]  # axis

            # y-axis
            avg_score_1st = round(year1['SCORE'].mean(),2)
            avg_score_2nd = round(year2['SCORE'].mean(),2)
            avg_score_3rd = round(year3['SCORE'].mean(),2)
            avg_score_4th = round(year4['SCORE'].mean(),2)
            scores = [avg_score_1st, avg_score_2nd, avg_score_3rd, avg_score_4th]  # axis

            plt.bar(years, scores)
            plt.title('Year-wise students avg score')
            plt.xticks(years,('1','2','3','4'))
            for x,y in zip(years,scores):
                plt.text(x,y,str(y),ha='center',color='blue')
            plt.xlabel('YEAR')
            plt.ylabel('AVG. SCORE')
            plt.show()

        else:
            print(f'1 or more file(s) missing!')

    except Exception as e:
        print(f'Missing file!\n{str(e)}')

def main():
    try:
        while True:
            print('\n===STUDENT SCORE ENTRY===')
            choice = int(input('\n1 - 1ST YEAR\n2 - 2ND YEAR\n3 - 3RD YEAR\n4 - 4TH YEAR\n5 - REPRESENTATION\n6 - EXIT\nENTER YOUR CHOICE (from 1 to 6) - \n'))
            if choice == 1:
                year_1()
            elif choice == 2:
                year_2()
            elif choice == 3:
                year_3()
            elif choice == 4:
                year_4()
            elif choice == 5:
                representation()
            elif choice == 6:
                print('Goodbye')
                break
            else:
                print('Invalid choice!')

    except Exception as e:
        print(f'Error!\n{str(e)}')

main()