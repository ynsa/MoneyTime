import numpy as np
from sklearn.tree import DecisionTreeClassifier

from django.db.models.signals import post_save
from django.dispatch import receiver

from MoneyTime.web.models import Expense


@receiver(post_save, sender=Expense)
def prediction(sender, **kwargs):
    tree = DecisionTreeClassifier()
    expenses = Expense.objects.all()[1:]
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
    expense = Expense.objects.all()[0]
    category = expense.category.pk if expense.category else 0
    location_category = expense.location.category.pk \
        if expense.location and expense.location.category else 0
    location = expense.location.pk \
        if expense.location and expense.location.location else 0
    x = [
        expense.created.weekday(),
        expense.created.day,
        # expense.created.time(),
        category,
        location_category,
        location
    ]
    prediction = tree.predict([x,])
    print('{0} {1}'.format(expense.created, expense.category))
    print(prediction)
    # pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6))
    # pl.xlim([0, 1])
    # pl.ylim([0, 1])
    # pl.xlabel('False Positive Rate')
    # pl.ylabel('True Positive Rate')
    # pl.title('Receiver operating characteristic example')
    # pl.legend(loc="lower right")
    # pl.show()
