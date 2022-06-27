from itertools import combinations
from datetime import datetime

from Employee import Employee


def createSchedule(line):
    schedule = {}
    for value in line.split(","):
        day = value[:2]
        hours = value[2:].split("-")
        start = datetime.strptime(hours[0], "%H:%M").time()
        end = datetime.strptime(hours[1], "%H:%M").time()
        schedule[day] = [start, end]
    return schedule


def loadfile(path):
    employees = []
    with open(path, 'r') as file:
        for line in file:
            name, schedule = line.strip().split("=")
            schedule = createSchedule(schedule)
            employee = Employee(name, schedule)
            employees.append(employee)
    return employees


def relations(employees):
    values = list(combinations(employees, 2))
    return values


def coincidence(employee, lista, count):
    if count < len(employee):
        employA, employB = employee[count]
        names = f"{employA.name}-{employB.name}"
        counter = intersection(employA.schedule, employB.schedule)
        lista.append(f"{names}:{counter}")
        coincidence(employee, lista, count + 1)
    return lista


def intersection(schedule1, schedule2):
    counter = 0
    for schedule in schedule1:
        if schedule in schedule2:
            cond1 = schedule1[schedule][0] == schedule2[schedule][0]
            cond2 = schedule1[schedule][1] == schedule2[schedule][1]
            cond3 = schedule2[schedule][0] < schedule1[schedule][0] < schedule2[schedule][1]
            cond4 = schedule2[schedule][0] < schedule1[schedule][1] < schedule2[schedule][1]
            cond5 = schedule1[schedule][0] < schedule2[schedule][0] < schedule1[schedule][1]
            cond6 = schedule1[schedule][0] < schedule2[schedule][1] < schedule1[schedule][1]
            if cond1 or cond2 or cond3 or cond4 or cond5 or cond6:
                counter += 1
    return counter
