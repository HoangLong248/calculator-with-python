from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/sum")
def multi_2_num():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        return jsonify(num1 * num2)
    except:
        raise

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)