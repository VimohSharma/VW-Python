
from flask import Flask, render_template, jsonify

app=Flask(__name__)

@app.route("/add/<int:num1>/<int:num2>")
def addition(num1,num2):
    return f"{num1} + {num2} = {num1+num2}"

if __name__ == "__main__":

    app.run(debug=True)
