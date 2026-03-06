from flask import jsonify, session, request, make_response
from . import products_bp
import json

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200},
    {"id": 4, "name": "Monitor", "price": 15000},
    {"id": 5, "name": "Headphones", "price": 2500},
    {"id": 6, "name": "Webcam", "price": 1800},
    {"id": 7, "name": "Printer", "price": 8500},
    {"id": 8, "name": "External Hard Drive", "price": 6000},
    {"id": 9, "name": "USB Flash Drive", "price": 700},
    {"id": 10, "name": "Gaming Chair", "price": 12000},
    {"id": 11, "name": "Graphics Card", "price": 45000},
    {"id": 12, "name": "Motherboard", "price": 14000},
    {"id": 13, "name": "RAM 16GB", "price": 5500},
    {"id": 14, "name": "SSD 1TB", "price": 7500},
    {"id": 15, "name": "Power Supply", "price": 4000}
]

@products_bp.route("/",methods=["GET"])
def get_products():
    return jsonify(products)

@products_bp.route("/<int:product_id>", methods=["GET"])
def view_product(product_id):

    if "user" not in session:
        return jsonify({"error": "User not logged in"}), 401

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    recent = request.cookies.get("recent_products")

    if recent:
        recent_list = json.loads(recent)
    else:
        recent_list = []

    if product_id in recent_list:
        recent_list.remove(product_id)

    recent_list.insert(0, product_id)

    recent_list = recent_list[:5]

    response = make_response(jsonify(product))
    response.set_cookie("recent_products", json.dumps(recent_list))

    return response


@products_bp.route("/recent", methods=["GET"])
def recent_products():

    recent = request.cookies.get("recent_products")

    if not recent:
        return jsonify([])

    ids = json.loads(recent)

    result = [p for p in products if p["id"] in ids]

    return jsonify(result)