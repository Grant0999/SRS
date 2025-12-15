import csv
from datetime import datetime, timedelta,date
import sys
import random
class Menu:
    def __init__ (self):
        self.inMenu = True
        while self.inMenu == True:
            try:
                menu = float(input('Weclome to Grantos SRS \n 1.Study \n 2.Add New Cards \n 3.Settings \n 4.Exit\n'))
                if menu == 1:
                    Study()
                elif menu == 2:
                    AddNewCards()
                elif menu == 3:
                    Settings()
                elif menu == 4:
                    sys.exit()

            except ValueError:
                print('Invalid Input')

class Study:
    def __init__(self):
        self.Studying=True
        self.studylogic()
    def studylogic(self):
        with open("Cards.csv", "r", newline='', encoding='utf-8') as icsv:
            reader = csv.reader(icsv)
            rows = list(reader)
        matching_rows = [row for row in rows if len(row) > 3 and datetime.strptime(row[2].strip(),"%Y-%m-%d").date() <= datetime.today().date()]
        if matching_rows:
            selected_row = random.choice(matching_rows)
            question = selected_row[0]
            answer = selected_row[1]
            date = selected_row[2]
            today = datetime.today().date()
            interval = int(selected_row[3])
            print(question)
            showanswer = float(input('1.Answer 2.Back To Menu\n'))
            if showanswer == 1:
                interval = 1
                date = today.strftime("%Y-%m-%d")
                print(answer)
            elif showanswer == 2:
                Menu()
                return
            passfail = float(input('1.Pass 2.Fail\n'))
            if passfail == 1:
                print('passed')
                interval = interval*2
                date = (datetime.strptime(date, "%Y-%m-%d").date() + timedelta(days=interval)).strftime("%Y-%m-%d")
            else:
                print('failed')
                if interval > 1:
                    interval = 1
                date = (datetime.strptime(date, "%Y-%m-%d").date() + timedelta(days=interval)).strftime("%Y-%m-%d")
            selected_row[2] = date
            selected_row[3] = str(int(interval))
            with open("Cards.csv", "w", newline='', encoding='utf-8') as icsv:
                writer = csv.writer(icsv)
                writer.writerows(rows)
            self.studylogic()
        else:
            print('No More Questions Today')
            self.Studying = False


class AddNewCards:
    def __init__(self):
        self.add_new_cards()

    def add_new_cards(self):
        self.wordsadded = 0
        self.addwords = True
        while self.addwords:
            word = str(input('Enter a word: '))
            definition = str(input('Enter a definition: '))
            interval = int(1)
            file_path = 'Cards.csv'
            with open(file_path, 'r') as file:
                line_count = sum(1 for line in file)
                linenumber = line_count
            with open(file_path, 'a', newline='\n') as file:
                file.write(word + ',' + definition + ',' + str(date.today()) + ',' + str(line_count) + ',' + str(
                    interval) + '\n')
            self.wordsadded += 1
            self.cont()
    def cont(self):
        print('Total Added This Session:', self.wordsadded, "\nAdd Another \n (y/n)?")
        ans = input()
        if ans == 'y':
            self.addwords = True
        elif ans == 'n':
            self.addwords = False

        else:
            print('Please enter y or n.')
            self.cont()

class Settings:
    def __init__ (self):
        settings = float(input('Settings: \n1.Wipe Deck \n2.Back To Menu\n'))
        if settings == 1:
            file_path = 'Cards.csv'
            with open(file_path, 'w') as file:
                fieldnames = ['Word', 'Def', 'Date', 'Line', 'Interval']
                file.write('')
                print(f"csv file '{file_path}' was Wiped")
        elif settings == 2:
            self.inSettings = False

class csv_creation:
    def __init__(self, file_path):
        file_path = 'Cards.csv'
        with open(file_path, 'a') as file:
            fieldnames = ['Word', 'Def', 'Date','Line', 'Interval']
            file.write(' \n')
            print(f"csv file '{file_path}' was created")
class Start:
    def __init__(self):
        try:
            file_path = 'Cards.csv'
            with open(file_path, 'r') as file:
                line_count = sum(1 for line in file)
                linenumber = line_count
                if line_count < 1:
                   pass
                else:
                    Menu()
        except FileNotFoundError:
            print('Creating New File...')
            csv_creation(file_path='Cards.csv')
            Menu()
Start()
