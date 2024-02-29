from flask import Flask

app = Flask(__name__)  # creates new Flask object


@app.route("/")  # maps the function to the route "/" (root)
def home() -> str:
    return "This is the home page!"


@app.route("/echo/<thing>")  # maps the function and sets an argument "thing"
def echo(thing: str) -> str:
    return f"Say hello to my parameter: {thing}"


app.run(port=9999, debug=True)