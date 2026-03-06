from flask import Flask, request, jsonify
from products import products_bp
from auth import auth_bp

app = Flask(__name__)
app.secret_key="secret2002"

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(products_bp, url_prefix="/products")

if __name__ == '__main__':
    app.run(debug=True)