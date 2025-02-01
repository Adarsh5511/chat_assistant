import sqlite3


conn = sqlite3.connect("company.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
''')


employees = [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20'),
    (4, 'Mishty', 'Sales', 90000, '2023-01-17'),
    (5, 'David', 'Engineering', 75000, '2019-09-10'),
    (6, 'Eva', 'Marketing', 55000, '2022-07-25'),
    (7, 'Frank', 'Sales', 60000, '2021-12-05'),
    (8, 'Grace', 'Engineering', 80000, '2020-03-30'),
    (9, 'Hannah', 'Marketing', 62000, '2021-08-10'),
    (10, 'Isaac', 'Sales', 58000, '2020-11-15'),
    (11, 'Jack', 'Engineering', 72000, '2019-05-02'),
    (12, 'Kara', 'Marketing', 65000, '2021-02-17'),
    (13, 'Liam', 'Sales', 64000, '2022-01-10'),
    (14, 'Mona', 'Engineering', 77000, '2020-09-05'),
    (15, 'Nina', 'Marketing', 59000, '2021-04-25'),
    (16, 'Oscar', 'Sales', 51000, '2023-03-12'),
    (17, 'Paul', 'Engineering', 73000, '2022-06-18'),
    (18, 'Quinn', 'Marketing', 61000, '2022-09-08'),
    (19, 'Rachel', 'Sales', 69000, '2021-11-01'),
    (20, 'Steve', 'Engineering', 76000, '2019-12-14')
]


cursor.executemany('''
    INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date)
    VALUES (?, ?, ?, ?, ?)
''', employees)


departments = [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie')
]

cursor.executemany('''
    INSERT INTO Departments (ID, Name, Manager)
    VALUES (?, ?, ?)
''', departments)


conn.commit()
conn.close()

print("Database 'company.db' created successfully with tables and sample data.")