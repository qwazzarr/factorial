from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial", methods=["POST"])
def endpoint():
    data = request.get_json()
    argument = data.get("argument")
    if argument is not None:
        result = calculate(argument)
        return {"result": result}, 200  # OK
    else:
        return "", 400  # Bad Request

def calculate(n):
    if n <= 0:
        return 1
    else:
        return n * calculate(n - 1)

if __name__ == "__main__":
    app.run(host="localhost", port=3000)

