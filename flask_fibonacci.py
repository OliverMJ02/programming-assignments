from flask import Flask, jsonify
from flask.wrappers import Response as FlaskResponse
from werkzeug.wrappers.response import Response as WerkzeugResponse

app = Flask(__name__)  # creates new Flask object

Response = str | FlaskResponse | WerkzeugResponse  # creates a Response type


def fibonacci_of(n: int) -> int:  # our function to compute the number
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


@app.route("/")  # maps the function to the route "/" (root)
def home() -> str:
    return "This is the home page!"


@app.route("/fibonacci/<int:number>")
def echo(number: int) -> Response:
    numbers = [fibonacci_of(n) for n in range(number)]
    return jsonify(numbers)


app.run(port=9999, debug=True)