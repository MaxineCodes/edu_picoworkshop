from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/temperature", methods=["POST"])
def temperature():
    """An endpoint accepting a temperature reading"""

    data = request.json  # temperature reading

    # if temperature exceeds a certain treshold (e.g. 20 °C),
    # reply with a warning so the client can set the red LED

    if data["temperature"] > 20:
        return jsonify({"warning": True})

    # else just reply all is well and maybe signal that
    # the red LED should be switched off

    else:
        return jsonify({"warning": False})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
