import tkinter as tk
import mysql.connector

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="school"
)

cursor = db.cursor()

# Functions
def add_student():
    id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    sql = "INSERT INTO students VALUES (%s,%s,%s,%s)"
    val = (id, name, age, course)

    cursor.execute(sql, val)
    db.commit()

    label_result.config(text="Student Added")

def show_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    text_box.delete(1.0, tk.END)

    for row in rows:
        text_box.insert(tk.END, str(row) + "\n")

# Tkinter Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

tk.Label(root, text="ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root)
entry_course.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Show Students", command=show_students).pack(pady=5)

text_box = tk.Text(root, height=10)
text_box.pack()

label_result = tk.Label(root, text="")
label_result.pack()


root.mainloop()