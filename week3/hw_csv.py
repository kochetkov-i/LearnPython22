import csv


users_jobs = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('users_jobs.csv', 'a', encoding='utf-8', newline='') as file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(file, fields, delimiter=';')
    writer.writeheader()
    for user in users_jobs:
        writer.writerow(user)