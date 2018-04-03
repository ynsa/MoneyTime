from datetime import datetime

from decimal import Decimal
from django.core.management import BaseCommand

import xlrd
import csv

from MoneyTime.web.models import Expense, ExpenseCategory, LocationCategory, \
    User, Location


def csv_from_excel():
    wb = xlrd.open_workbook('timetable.xlsx')
    sh = wb.sheet_by_name('Лист1')
    your_csv_file = open('timetable.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


def create_stats(filename, user_pk):
    user = User.objects.get(pk=user_pk)
    with open(filename, newline='', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in reader:
            count += 1
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])
            print(row[5])
            print('----------')
            expense = Expense(user=user)
            expense.save()
            datet = datetime.strptime(row[0][1:] if count == 1 else row[0], '%d.%m.%Y %H:%M')
            # datet = datetime.strptime((row[0][1:] if len(row[0]) > 10 else row[0]) + ' ' + row[1], '%d.%m.%Y %H:%M')
            ex_cat = row[2]
            loc_name = row[3]
            loc_cat = row[4]
            # if len(row) > 5:
            #     expense.amount = Decimal(row[5])
            print(loc_cat)
            if len(ex_cat) != 0:
                expense_cat, created = ExpenseCategory.objects.get_or_create(
                    user=user,
                    name=ex_cat
                )
            else:
                expense_cat, created = ExpenseCategory.objects.get_or_create(
                    user=user,
                    name='Undefined'
                )
            print(expense_cat)
            expense.category = expense_cat
            if len(loc_cat) != 0:
                location_cat, created = LocationCategory.objects.get_or_create(
                    user=user,
                    name=loc_cat
                )
            # expense.location_category = location_cat
            if len(loc_name) != 0 or len(loc_cat) != 0:
                location_cat_def, created = LocationCategory.objects.get_or_create(
                    user=user,
                    name='Undefined'
                )
                location, created = Location.objects.get_or_create(
                    user=user,
                    name=loc_name if len(loc_name) else 'Undefined',
                    category=location_cat if len(loc_cat) else location_cat_def
                )
                print(location)
                expense.location = location
            expense.created = datet
            print(expense.created)
            expense.save()


class Command(BaseCommand):
    help = 'Run create_stats'

    def handle(self, *args, **options):
        # csv_from_excel()
        filename = 'timetable_2.txt'
        create_stats(filename, 1)
