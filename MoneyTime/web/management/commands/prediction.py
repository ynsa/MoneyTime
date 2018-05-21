import csv
from django.core.management import BaseCommand
from pytz import utc
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import auc, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import pickle
import datetime
import pandas as pd
import pylab as pl
import numpy as np
from MoneyTime.web.models import Expense, Prediction, ExpenseCategory


def date_to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


def time_to_integer(dt_time):
    return 10000*dt_time.hour + 100*dt_time.minute + dt_time.second


def create_data(expense):
    category = expense.category.pk if expense.category else 0
    location_category = expense.location.category.pk \
        if expense.location and expense.location.category else 0
    location = expense.location.pk \
        if expense.location and expense.location.location else 0
    return [
        expense.created.weekday() in (5, 6),
        date_to_integer(expense.created),
        category,
        location_category,
        location,
        time_to_integer(expense.created)
    ]


def write_to_file():
    expenses_full = Expense.objects.all()
    expenses = []
    for expense in expenses_full:
        expenses.append(create_data(expense))
    print(expenses[0])
    df = np.array(expenses)
    df = pd.DataFrame(df)
    df.to_csv('data_2.csv', sep='\t', encoding='utf-8')
    # with open('data.txt', "w") as output:
    #     writer = csv.writer(output, lineterminator='')
    #     print(writer)
    #     writer.writerows(expenses)


def create_x_data(expense):
    category = expense.category.pk if expense.category else 0
    location_category = expense.location.category.pk \
        if expense.location and expense.location.category else 0
    location = expense.location.pk \
        if expense.location and expense.location.location else 0
    # [day of week, date, time, expense category, location category, location]
    arr = [
        expense.created.weekday(),
        date_to_integer(expense.created),
        # expense.created.day,
        # expense.created.month,
        # expense.created.time(),
        category,
        location_category,
        location
    ]
    return arr


def convert_predicted_time(date, prediction):
    hour = int(prediction / 10000)
    minute = int((prediction - hour * 10000) / 100)
    second = int((prediction - hour * 10000 - minute * 100))
    if minute > 59:
        hour += 1
        minute -= 60
    if second > 59:
        minute += 1
        second -= 60
    time = datetime.datetime(
        date.year,
        date.month,
        date.day,
        hour,
        minute,
        second,
        tzinfo=utc
    )
    return time


def prediction_two(classifier=DecisionTreeRegressor(), filename='tree_classifier.pkl'):
    tree = classifier
    expenses_full = Expense.objects.all()
    # expences = np.zeros(6, expenses_full.count())
    x_train = []
    y_train = []
    for expense in expenses_full[:100]:
        # fields =
        x_train.append(create_x_data(expense))
        y_train.append(time_to_integer(expense.created))

    x_test = []
    y_test = []
    for expense in expenses_full[100:]:
        # fields =
        x_test.append(create_x_data(expense))
        y_test.append(time_to_integer(expense.created))
    # file = "data.txt"
    # df = pd.read_csv(file)
    # df.drop(['Country', 'Language', 'Rating', 'Poster'], axis=1, inplace=True)
    # target = df.created.values
    # train = df.drop('created', axis=1).values
    # coder = PCA(n_components=3)
    # train = coder.fit_transform(train)
    # TRNtrain, TRNtest, TARtrain, TARtest = train_test_split(train, target,
    #                                                         test_size=0.3,
    #                                                         random_state=0)
    tree = classifier
    tree = tree.fit(x_train, y_train)
    # a = tree.predict(x_test)  # предсказание
    from sklearn import tree as skl_tree
    import graphviz
    dot_data = skl_tree.export_graphviz(tree, out_file='RandomForestRegressor_500.dot')
    # print("AUC-ROC (oob) = ", roc_auc_score(y_train, tree.oob_prediction_))
    # print("AUC-ROC (test) = ", roc_auc_score(y_test, a))
    # pred_scr = tree.predict_proba(TRNtest)[:, 1]
    # fpr, tpr, thresholds = roc_curve(TARtest, pred_scr)
    #    roc_auc = auc(TARtest, pred_scr)
    # roc_auc = auc(fpr, tpr)
    # md = str(tree)
    # md = md[:md.find('(')]
    # pl.plot(fpr, tpr, label='ROC fold %s (auc = %0.2f)' % (md, roc_auc))



def prediction(classifier=DecisionTreeClassifier(), filename='tree_classifier.pkl'):
    # tree = DecisionTreeClassifier()
    tree = classifier
    expenses_full = Expense.objects.all()
    exp = expenses_full[:50]
    for expense_exl in exp:
        expenses = expenses_full.exclude(pk=expense_exl.pk)
        x_train = []
        y_train = []
        for expense in expenses:
            category = expense.category.pk if expense.category else 0
            location_category = expense.location.category.pk \
                if expense.location and expense.location.category else 0
            location = expense.location.pk \
                if expense.location and expense.location.location else 0
            # [day of week, date, time, expense category, location category, location]
            arr = [
                expense.created.weekday(),
                date_to_integer(expense.created),
                # expense.created.day,
                # expense.created.month,
                # expense.created.time(),
                category,
                location_category,
                location
            ]
            x_train.append(arr)
            # y.append(np.datetime64(expense.created))
            y_train.append(time_to_integer(expense.created))
            # y.append(np.datetime64(expense.created.time()))

        # np.nan_to_num(x, copy=False)
        # y = y.astype('datetime64[ns]')
        tree = tree.fit(x_train, y_train)
        # expense = Expense.objects.all()[0]
        expense = expense_exl
        category = expense.category.pk if expense.category else 0
        location_category = expense.location.category.pk \
            if expense.location and expense.location.category else 0
        location = expense.location.pk \
            if expense.location and expense.location.location else 0
        x = [
            expense.created.weekday(),
            date_to_integer(expense.created),
            # expense.created.day,
            # expense.created.month,
            # expense.created.time(),
            category,
            location_category,
            location
        ]
        prediction = tree.predict([x,])
        print('{0:>11} {1:26}  {2}'.format('Real:', str(expense.created), expense.category))
        # print('{0:>11} {1:>26}'.format('Predicted:', str(prediction[0])))
        print()
        import graphviz
        from sklearn import tree as skl_tree
        dot_data = skl_tree.export_graphviz(tree,
                                            out_file='RandomForestRegressor_500.dot')
        # pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6))
        # pl.xlim([0, 1])
        # pl.ylim([0, 1])
        # pl.xlabel('False Positive Rate')
        # pl.ylabel('True Positive Rate')
        # pl.title('Receiver operating characteristic example')
        # pl.legend(loc="lower right")
        # pl.show()
    #     hour = int(prediction[0] / 10000)
    #     minute = int((prediction[0] - hour * 10000) / 100)
    #     second = int((prediction[0] - hour * 10000 - minute * 100))
    #     if minute > 59:
    #         hour += 1
    #         minute -= 60
    #     if second > 59:
    #         minute += 1
    #         second -= 60
    #     time = datetime.datetime(
    #         expense.created.year,
    #         expense.created.month,
    #         expense.created.day,
    #         hour,
    #         minute,
    #         second,
    #         tzinfo=utc
    #     )
    #     start_time = expense.created.replace(tzinfo=utc)
    #     end_time = time.replace(tzinfo=utc)
    #     print('{0:>11} {1:>26}'.format('Predicted:', str(end_time)))
    #     print(end_time - start_time if end_time > start_time else str(start_time - end_time) + '   -')
    #     prediction_model = Prediction.objects.create(
    #         user_id=1,
    #         category=expense.category,
    #         predicted=time,
    #         applied=expense.created
    #     )
    #     print('----------------\n')
    # with open(filename, 'wb') as file:
    #     pickle.dump(tree, file)


def predict_new(date, category=0, location_category=0, location=0):
    with open('tree_classifier.pkl', 'rb') as file:
        tree = pickle.load(file)
    x = [
        date.weekday(),
        date_to_integer(date),
        category,
        location_category,
        location
    ]
    prediction = tree.predict([x, ])
    hour = int(prediction[0] / 10000)
    minute = int((prediction[0] - hour * 10000) / 100)
    second = int((prediction[0] - hour * 10000 - minute * 100))
    time = datetime.datetime(
        date.year,
        date.month,
        date.day,
        hour,
        minute,
        second,
        tzinfo=utc
    )
    prediction_model = Prediction.objects.create(
        user_id=1,
        category=ExpenseCategory.objects.get(pk=category),
        predicted=time,
    )
    print('----------------\n')


class Command(BaseCommand):
    help = 'Run prediction'

    def handle(self, *args, **options):
        # csv_from_excel()
        # prediction()
        # predict_new(datetime.datetime(2018, 5, 7), 16, 21, 24)
        # classifier = RandomForestClassifier(n_estimators=100, oob_score=True,
        #                         random_state=123456)
        # prediction(classifier, 'random_forest_classifier.pkl')
        classifier = RandomForestRegressor(n_estimators=500, oob_score=True, random_state=0)
        # prediction(classifier, 'random_forest_regressor_classifier.pkl')
        # write_to_file()
        prediction(classifier)
