import numpy as np
from django.core.management import BaseCommand
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import pylab as pl

from django.db.models.signals import post_save
from django.dispatch import receiver

from MoneyTime.web.models import Expense

def prediction():
    tree = DecisionTreeClassifier()
    expenses_full = Expense.objects.all()
    for expense_exl in expenses_full:
        expenses = expenses_full.exclude(pk=expense_exl.pk)
        x = []
        y = []
        for expense in expenses:
            category = expense.category.pk if expense.category else 0
            location_category = expense.location.category.pk \
                if expense.location and expense.location.category else 0
            location = expense.location.pk \
                if expense.location and expense.location.location else 0
            # [day of week, date, time, expense category, location category, location]
            arr = [
                expense.created.weekday(),
                expense.created.day,
                expense.created.month,
                # expense.created.time(),
                category,
                location_category,
                location
            ]
            x.append(arr)
            y.append(np.datetime64(expense.created))
            # y.append(np.datetime64(expense.created.time()))

        # np.nan_to_num(x, copy=False)
        # y = y.astype('datetime64[ns]')
        tree = tree.fit(x, y)
        # expense = Expense.objects.all()[0]
        expense = expense_exl
        category = expense.category.pk if expense.category else 0
        location_category = expense.location.category.pk \
            if expense.location and expense.location.category else 0
        location = expense.location.pk \
            if expense.location and expense.location.location else 0
        x = [
            expense.created.weekday(),
            expense.created.day,
            expense.created.month,
            # expense.created.time(),
            category,
            location_category,
            location
        ]
        prediction = tree.predict([x,])
        print('{0:>11} {1:26}  {2}'.format('Real:', str(expense.created), expense.category))
        print('{0:>11} {1:>26}'.format('Predicted:', str(prediction[0])))
        print()
        pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6))
        pl.xlim([0, 1])
        pl.ylim([0, 1])
        pl.xlabel('False Positive Rate')
        pl.ylabel('True Positive Rate')
        pl.title('Receiver operating characteristic example')
        pl.legend(loc="lower right")
        # pl.show()


class Command(BaseCommand):
    help = 'Run prediction'

    def handle(self, *args, **options):
        # csv_from_excel()
        prediction()