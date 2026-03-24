from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        length = float(request.form.get("length"))
        width = float(request.form.get("width"))

        area = length * width
        waste_factor = 1.1
        total_area = area * waste_factor

        result = round(total_area, 2)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)