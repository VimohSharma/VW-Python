from flask import request,session,jsonify
from . import auth_bp

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    session["user"] = username

    return jsonify({
        "message": "Login successful",
        "user": username
    })