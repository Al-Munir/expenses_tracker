import csv
import gspread
import time


MONTH = input('Enter the month and year you wish to extract in MM-YYYY format: ')
MNTH = input('Enter first three letters of Month in CAPS: ')

file = f'{MONTH}.csv'

transactions = []

def hsbcFin(file):

    with open(file, mode ='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            description = str(row[1]).lower()
            description2 = description.upper()
            amount1 = row[2]
            amount2 = amount1.replace(',','')
            amount = float(amount2)
            category = 'Other'

            if 'just eat co uk ltd' in description:
                category = 'WAGES'

            elif 'eat' in description:
                category = 'FOOD'  

            elif 'food' in description:
                category = 'FOOD'  

            elif 'takeaway' in description:
                category = 'FOOD' 

            elif 'ee limited' in description:
                category = 'MOBILE'  

            elif 'gift' in description:
                category = 'GIFT' 

            elif 'amz' in description:
                category = 'PURCHASES' 

            elif 'tower hamlets' in description:
                category = 'RENT' 

            elif 'tfl' in description:
                category = 'TRAVEL' 

            elif 'cash' in description:
                category = 'CASH WITHDRAWAL' 

            elif 'minted' in description:
                category = 'INVESTMENTS' 
            
            elif 'cinema' in description:
                category = 'ENTERTAINMENT'
            
            elif 'udemy' in description:
                category = 'COURSE SUBSCRIPTIONS'  

            elif 'coursra' in description:
                category = 'COURSE SUBSCRIPTIONS'  

            elif 'wedding' in description:
                category = 'WEDDING EXPENSES'  

            elif 'london borough of london vis' in description:
                category = 'TRAVEL'  

            elif 'paypal' in description:
                category = 'PURCHASES'  

            transaction = ((date, description2, amount, category))
            print(transaction)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open('Expenses Tracker')

wks = sh.worksheet(f'{MNTH}')

rows = hsbcFin(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2]],2)
    time.sleep(1)


