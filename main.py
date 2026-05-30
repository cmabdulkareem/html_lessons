import mysql.connector

# ----------------------------
# CONNECT TO MYSQL SERVER
# ----------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"      # Change if needed
)

cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")

# Select database
cursor.execute("USE student_db")

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100)
)
""")

conn.commit()

# ----------------------------
# MENU
# ----------------------------

while True:

    print("\n==============================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    # ADD
    if choice == "1":

        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")

        sql = """
        INSERT INTO students(name, age, course)
        VALUES(%s, %s, %s)
        """

        cursor.execute(sql, (name, age, course))
        conn.commit()

        print("✓ Student Added Successfully")

    # VIEW
    elif choice == "2":

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        print("\nID\tNAME\tAGE\tCOURSE")
        print("-" * 50)

        for s in students:
            print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}")

    # UPDATE
    elif choice == "3":

        sid = int(input("Student ID: "))

        name = input("New Name: ")
        age = int(input("New Age: "))
        course = input("New Course: ")

        sql = """
        UPDATE students
        SET name=%s, age=%s, course=%s
        WHERE id=%s
        """

        cursor.execute(sql, (name, age, course, sid))
        conn.commit()

        print("✓ Student Updated Successfully")

    # DELETE
    elif choice == "4":

        sid = int(input("Student ID: "))

        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (sid,)
        )

        conn.commit()

        print("✓ Student Deleted Successfully")

    # SEARCH
    elif choice == "5":

        keyword = input("Enter Name: ")

        cursor.execute(
            "SELECT * FROM students WHERE name LIKE %s",
            ("%" + keyword + "%",)
        )

        students = cursor.fetchall()

        print("\nID\tNAME\tAGE\tCOURSE")
        print("-" * 50)

        for s in students:
            print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}")

    # EXIT
    elif choice == "6":

        print("Goodbye!")
        break

    else:
        print("Invalid Choice")

# Close connection
cursor.close()
conn.close()