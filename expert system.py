import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="employee_db"
)
cursor = conn.cursor()

# CREATE
def add_employee():
    name = input("Name: ")
    p = int(input("Punctuality: "))
    w = int(input("Work Quality: "))
    t = int(input("Teamwork: "))
    avg = (p + w + t) / 3

    if avg >= 85:
        eval = "Excellent"
    elif avg >= 70:
        eval = "Good"
    else:
        eval = "Needs Improvement"

    query = "INSERT INTO Employees (name, punctuality, work_quality, teamwork, evaluation) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, p, w, t, eval))
    conn.commit()
    print("Added.\n")

# READ
def show_employees():
    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        print(row)
    print()

# UPDATE
def update_name():
    id = input("ID to update: ")
    new_name = input("New name: ")
    cursor.execute("UPDATE Employees SET name = %s WHERE id = %s", (new_name, id))
    conn.commit()
    print("Updated.\n")

# DELETE
def delete_employee():
    id = input("ID to delete: ")
    cursor.execute("DELETE FROM Employees WHERE id = %s", (id,))
    conn.commit()
    print("Deleted.\n")

# Menu
while True:
    print("1. Add  2. Show  3. Update  4. Delete  5. Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_employee()
    elif ch == "2":
        show_employees()
    elif ch == "3":
        update_name()
    elif ch == "4":
        delete_employee()
    elif ch == "5":
        break
    else:
        print("Invalid.")

cursor.close()
conn.close()
