from flask import Flask, render_template

app = Flask(__name__)

@app.route("/students")
def show_students():

    students = [
        {"name": "John", "marks": 33},
        {"name": "Amit", "marks": 62},
        {"name": "Priya", "marks": 55},
        {"name": "Jiya", "marks": 62},
        {"name": "Singh", "marks": 42}
        ]

    return render_template("students.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)