from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo")
def show():
    return render_template("list.html", names=["arun","priya","amit"])


if __name__ == "__main__":
    app.run(debug=True)