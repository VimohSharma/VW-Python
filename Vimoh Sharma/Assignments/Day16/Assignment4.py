from flask import Flask, render_template, request

app=Flask(__name__)

products = [
    {"name": "Laptop", "category": "Electronics", "price": 50000, "available": True},
    {"name": "Phone", "category": "Electronics", "price": 20000, "available": False},
    {"name": "Book", "category": "Books", "price": 500, "available": True},
    {"name": "Pen", "category": "Stationery", "price": 50, "available": True},
]

@app.route("/products")
def show_products():

    filtered_lis=products.copy()

    cat=request.args.get("category")
    available=request.args.get("available")
    sorting=request.args.get("sort")

    if cat:
        filtered_lis=[prod for prod in filtered_lis if prod["category"] == cat]

    if available:
            if available.lower()=="true":
                filtered_lis=[prod for prod in filtered_lis if prod["available"]]

    if sorting:
        if sorting == "low":
            filtered_lis=sorted(filtered_lis, key=lambda x:x["price"])
        elif sorting == "high":
            filtered_lis=sorted(filtered_lis, key=lambda x:x["price"], reverse=True)
    
    cnt=len(filtered_lis)

    return render_template("prod.html", products=filtered_lis, count=cnt)

if __name__ == "__main__":
    app.run(debug=True)