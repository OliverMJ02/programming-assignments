from flask import Flask

app = Flask(__name__)  # creates new Flask object


@app.route("/")  # maps the function to the route "/" (root)
def home() -> str:
    print("this comes from my code")
    return "This is the home page!"


@app.route("/echo/<thing>")  # maps the function and sets an argument "thing"
def echo(thing: str) -> str:
    return f"Parameter received: {thing}"


def test() -> str:
    return "This is a test!"


@app.route("/dictionary")
def dictionary() -> dict[str, str]:
    result = {
        "name": "Applied OOP",
        "code": "EEN060"
    }
    return result


print("Preparing to run...")
app.run(port=9998, debug=True)
