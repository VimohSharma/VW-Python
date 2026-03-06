from flask import Flask, request, jsonify
import csv
import io

app = Flask(__name__)

# In-memory storage
products = []


@app.route('/upload', methods=['POST'])
def upload_csv():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    csv_reader = csv.DictReader(stream)

    total_rows = 0
    products_added = 0
    failed_rows = 0

    for row in csv_reader:
        total_rows += 1

        name = row.get("name")
        price = row.get("price")
        stock = row.get("stock")

        try:
            # Validation
            if not name or name.strip() == "":
                raise ValueError("Invalid name")

            price = float(price)
            if price <= 0:
                raise ValueError("Invalid price")

            stock = int(stock)
            if stock < 0:
                raise ValueError("Invalid stock")

            product = {
                "name": name,
                "price": price,
                "stock": stock
            }

            products.append(product)
            products_added += 1

        except:
            failed_rows += 1

    return jsonify({
        "total_rows": total_rows,
        "products_added": products_added,
        "failed_rows": failed_rows
    })


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)