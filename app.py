from flask import Flask, render_template, request
from rent_calculator import calculate_per_person

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    values = {
        "rent": "",
        "food": "",
        "electricity_units": "",
        "charge_per_unit": "",
        "people": "",
    }

    if request.method == "POST":
        values = {key: request.form.get(key, "").strip() for key in values}
        try:
            numbers = {key: int(value) for key, value in values.items()}
            result = calculate_per_person(
                rent=numbers["rent"],
                food=numbers["food"],
                electricity_units=numbers["electricity_units"],
                charge_per_unit=numbers["charge_per_unit"],
                people=numbers["people"],
            )
            result["people"] = numbers["people"]
        except ValueError as exc:
            error = str(exc) or "Please enter valid whole numbers in every field."

    return render_template("index.html", result=result, error=error, values=values)

if __name__ == "__main__":
    app.run(debug=True)
