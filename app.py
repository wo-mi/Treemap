import json
from flask import Flask, render_template

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/data")
def data():
    with open("dummy_data.json", "r", encoding="utf8") as f:
        dummy_data = json.load(f)

    return dummy_data


@app.route("/item/<int:id>")
def item(id):
    return f"<b>ID: {id}</b>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
