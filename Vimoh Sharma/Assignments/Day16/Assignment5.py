from flask import Flask, render_template, request

app = Flask(__name__)

employees = [
    {"name": "John", "salary": 50000},
    {"name": "Amit", "salary": 40000},
    {"name": "Jonathon", "salary": 45000},
    {"name": "Price", "salary": 90000},
    {"name": "Noir", "salary": 78000},
    {"name": "Loira", "salary": 25000},
    {"name": "Stuart", "salary": 35000},
    {"name": "Vips", "salary": 95000},
]


@app.route("/dashboard")
def dashboard():

    role = request.args.get("role", "employee")

    return render_template(
        "dashboard.html",
        role=role,
        employees=employees
    )


if __name__ == "__main__":
    app.run(debug=True)