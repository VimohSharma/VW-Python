from flask import Blueprint, request, jsonify
from ..models import Order
from .. import db

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/orders", methods=["POST"])
def add_order():

    data = request.json

    order = Order(
        product_name=data["product_name"],
        quantity=data["quantity"],
        price=data["price"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order added"})

@orders_bp.route("/orders", methods=["GET"])
def list_orders():

    orders = Order.query.all()

    result = []

    for o in orders:

        revenue = o.price * o.quantity

        result.append({
            "id": o.id,
            "product_name": o.product_name,
            "quantity": o.quantity,
            "price": o.price,
            "revenue": revenue
        })

    return jsonify(result)

@orders_bp.route("/orders/total-revenue")
def total_revenue():

    orders = Order.query.all()

    total = 0

    for o in orders:
        total += o.price * o.quantity

    return jsonify({"total_revenue": total})

@orders_bp.route("/orders/high")
def high_revenue_orders():

    orders = Order.query.all()

    result = []

    for o in orders:

        revenue = o.price * o.quantity

        if revenue > 2000:
            result.append({
                "product_name": o.product_name,
                "revenue": revenue
            })

    return jsonify(result)