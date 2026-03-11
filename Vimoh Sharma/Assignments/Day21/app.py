from flask import Flask, request, session, jsonify
from flask_migrate import Migrate
from models import db, User, Employee
from decorators import role_required

app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Momdad2002!@localhost:3006/day21"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def home():
    return "Employee Portal Running"

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(
        username=data["username"],
        password=data["password"]
    ).first()

    if user:

        session["user_id"] = user.id
        session["role"] = user.role

        return jsonify({
            "message": "Login successful",
            "role": user.role
        })

    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/employees", methods=["GET"])
@role_required(["Admin", "Manager"])
def get_employees():

    employees = Employee.query.all()

    result = []

    for emp in employees:
        result.append({
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "department": emp.department,
            "manager_id": emp.manager_id
        })

    return jsonify(result)

@app.route("/employee/<int:id>", methods=["GET"])
@role_required(["Admin", "Manager", "Employee"])
def get_employee(id):

    emp = Employee.query.get(id)

    if not emp:
        return jsonify({"message": "Employee not found"}), 404

    return jsonify({
        "id": emp.id,
        "name": emp.name,
        "email": emp.email,
        "department": emp.department,
        "manager_id": emp.manager_id
    })

@app.route("/employee/<int:id>/edit", methods=["PUT"])
@role_required(["Admin", "Manager", "Employee"])
def edit_employee(id):

    emp = Employee.query.get(id)

    if not emp:
        return jsonify({"message": "Employee not found"}), 404

    role = session["role"]
    user_id = session["user_id"]

    # Admin can edit anyone
    if role == "Admin":
        pass

    # Manager can edit only their employees
    elif role == "Manager":
        if emp.manager_id != user_id:
            return jsonify({"message": "Managers can only edit their team"}), 403

    # Employee can edit only themselves
    elif role == "Employee":
        if emp.id != user_id:
            return jsonify({"message": "Employees can edit only their own profile"}), 403

    data = request.json

    emp.name = data.get("name", emp.name)
    emp.email = data.get("email", emp.email)
    emp.department = data.get("department", emp.department)

    db.session.commit()

    return jsonify({"message": "Employee updated successfully"})

@app.route("/employee/<int:id>/delete", methods=["DELETE"])
@role_required(["Admin"])
def delete_employee(id):

    emp = Employee.query.get(id)

    if not emp:
        return jsonify({"message": "Employee not found"}), 404

    db.session.delete(emp)
    db.session.commit()

    return jsonify({"message": "Employee deleted successfully"})

@app.route("/logout")
def logout():

    session.clear()

    return jsonify({"message": "Logged out successfully"})

if __name__ == "__main__":
    app.run(debug=True)