import csv, sys, os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))

# project_dir = "C:/Users/NishantDas/Desktop/Loaddata/salarydata"
# sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'salarydata.settings'

import django

django.setup()

from salaryapp.models import Data

file = csv.reader(open("data.csv"),delimiter=",")

for row in file:
    data = Data()
    data.age = row[0]
    data.workclass = row[1]
    data.fnlwgt = row[2]
    data.education = row[3]
    data.education_num = row[4]
    data.martial_status = row[5]
    data.occupation = row[6]
    data.relationship = row[7]
    data.race = row[8]
    data.sex = row[9]
    data.capital_gain = row[10]
    data.capital_loss = row[11]
    data.hours_per_week = row[12]
    data.native_country = row[13]
    data.salary_choices = row[14]
    data.save()
    