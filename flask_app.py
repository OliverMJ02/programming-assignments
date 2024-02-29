# solution cell

from flask import Flask, jsonify
from flask.wrappers import Response as FlaskResponse
from werkzeug.wrappers.response import Response as WerkzeugResponse

# creates a Response type to be used as the return type of the function
Response = str | FlaskResponse | WerkzeugResponse

app = Flask(__name__)


### BEGIN SOLUTION
@app.route("/composite/<quantity>", methods=["GET"])
def get_composite_numbers(quantity: str) -> Response:
    try:
        q: int = int(quantity)
        comp_num: list[int] = []
        num = 4
        while len(comp_num) < q:
            if any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)):
                comp_num.append(num)
            num += 1
        return jsonify(comp_num)
    except ValueError:
        return jsonify([])


### END SOLUTION
