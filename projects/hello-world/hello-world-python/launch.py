from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Hello varshitha Python v1\"}"
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("7000"), debug=True)