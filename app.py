from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Message from Leo"

if __name__ == "__main__":
    app.run(port=80)
