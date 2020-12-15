"""
Time-table createing
"""
import os
import time


# This functin allows the user to enter the hours of each school day
# IN: ---
# OUT: times (list)
def time_table():
    lst = []
    times = []
    week_days = ('Monday?', 'Tuesday?', 'Wednesday?', 'Thursday?', 'Friday?')
    i = 0
    while i < len(week_days):
        print('How much hours you spent in school on',week_days[i])
        hours = int(input(': '))
        os.system('cls')
        if hours >= 1 and hours <= 12:
            times.append(hours)
            i += 1
        else:
            print('Thats not a possible answer of school hours!')
    lst.append(times)
    return lst


# The user can enter the subjects for each day
# IN: hour_lst (list)
# OUT: ---
def subject_table(hour_lst):
    hour_list = hour_lst
    day_lst = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    j = 0
    for hour in hour_lst[0]:
        i = 0
        subject_lst = []
        while i < hour:
            print('Here you can enter the name of the subject in a shorter version (z.b. German = G, maximum = 5 chars),',day_lst[j])
            subject = input(': ')
            os.system('cls')
            if len(subject) <= 5:
                subject_lst.append(subject.upper())
                i += 1
            else:
                print('The name that you entered is too long! (maximum = 5 chars)')
                print('Please try again')
                time.sleep(1)
        hour_list.append(subject_lst)
        j += 1
    hour_list.pop(0)
    return hour_list
        

# This function generates a time-table with all the informations
# IN: hours_subjects 
# OUT: ---
def create_time_table(hours_subjects):
    subject_length = 5 * ' '
    print(31 * '-')
    print('| MON | TUE | WED | THUR| FRI |')
    print(31 * '-')
    j_t = False
    k_t = False
    l_t = False
    m_t = False
    n_t = False
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    while not j_t or not k_t or not l_t or not m_t or not n_t:
        i = 0
        if j < len(hours_subjects[i]):
            print('|' + (hours_subjects[i][j] + ((len(subject_length) - len(hours_subjects[i][j]))) * ' '), end='|')
            i += 1
        elif j_t:
            print('|' + 5 * ' ',end='|')
            i += 1
        else:
            j_t = True
            print('|' + 5 * ' ',end='|')
            i += 1
        if k < len(hours_subjects[i]):
            print(hours_subjects[i][k] + ((len(subject_length) - len(hours_subjects[i][k])) * ' '), end='|')
            i += 1
        elif k_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            k_t = True
            print(5 * ' ',end='|')
            i += 1
        if l < len(hours_subjects[i]):
            print(hours_subjects[i][l] + ((len(subject_length) - len(hours_subjects[i][l])) * ' '), end='|')
            i += 1
        elif l_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            l_t = True
            print(5 * ' ',end='|')
            i += 1
        if m < len(hours_subjects[i]):
            print(hours_subjects[i][m] + ((len(subject_length) - len(hours_subjects[i][m])) * ' '), end='|')
            i += 1
        elif m_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            m_t = True
            print(5 * ' ',end='|')
            i += 1
        if n < len(hours_subjects[i]):
            print(hours_subjects[i][n] + ((len(subject_length) - len(hours_subjects[i][n])) * ' '), end='|')
            i += 1
        elif  n_t:
            print(5 * ' ',end='|')
            i += 1
        else:
            n_t = True
            print(5 * ' ',end='|')
            i += 1
        print('')
        j += 1
        k += 1
        l += 1
        m += 1
        n += 1 
    return



# ===============================================================================================================================================
# ================================================================= MAIN ========================================================================
# ===============================================================================================================================================
os.system('cls')
hour_table = time_table()
subjects_and_hours = subject_table(hour_table)
os.system('cls')
create_time_table(subjects_and_hours)