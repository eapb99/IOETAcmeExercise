# ACME Exercise

## Description 

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

**Input**
the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

### Example1

#### Input
```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
``` 
#### Output
```
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```

### Example2

#### Input
```
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
``` 
#### Output
```
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```

## Programs and dependencies

- [Python 3.9.13](https://www.python.org/downloads/release/python-3913/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Unittest](https://docs.python.org/3/library/unittest.html)
FALTA

## Architecture



FlowChart|Entity Diagram
---|---
![image](https://user-images.githubusercontent.com/62962507/176063191-ab53af04-66d4-4ff6-9be5-83a8a5fa4550.png)|![image](https://user-images.githubusercontent.com/62962507/176063234-6d3d17db-737f-44ce-aeba-0de396a91ff4.png)


**loadfile(path)** -> This function receives the path of the file where the employee information is located and returns a list of employee objects.

**createSchedule(line)** -> This function receives a string with the information of the weekly hours of each employee and returns a dictionary, where the key is the day and the values are lists that contain the start and end time of that day.

**relations(employees)** -> This function receives a list of employees and generates all possible combination pairs for each employee without repeating.

**coincidence(employee, pairs, count)** -> Recursive function that goes through a list of employees and returns the pairs of employees with the number of matches in their schedules.

**intersection(schedule1, schedule2)** -> Function that receives two schedules of 2 employees and returns the number of times they are in the company
## Run Locally

To execute the solution of this project we must follow the following steps:
```
git clone https://github.com/eapb99/IOETAcmeExercise
cd IOETAcmeExercise
```

To execute the main.py it can be done in the IDE of preference or by python console.
```
python main.py 
```



