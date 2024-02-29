"""
A sample Hello World server.
"""
import os

from flask import Flask
from flask import send_file
from flask import request

import base64

# pylint: disable=C0103
app = Flask(__name__)


def decode_from_base64(encoded_string):
    # Convert the base64-encoded string to bytes
    encoded_bytes = encoded_string.encode("utf-8")
    # Base64 decode the bytes
    decoded_bytes = base64.b64decode(encoded_bytes)
    # Convert the decoded bytes back to a UTF-8 string
    decoded_string = decoded_bytes.decode("utf-8")
    return decoded_string


# Make use of POST request:
@app.route("/post", methods=["GET", "POST"])
def hello():
    """Get Cloud Run environment variables."""
    service = os.environ.get("K_SERVICE", "Unknown service")
    revision = os.environ.get("K_REVISION", "Unknown revision")

    if request.method == "POST":
        data = request.form
        with open("in.geojson", "w") as f:
            f.write(decode_from_base64(data["param1"]))

        # Return file in.geojson:
        return send_file("in.geojson", as_attachment=True)

    if request.method == "GET":
        return "GET request received!??sadfgasdf!!"


if __name__ == "__main__":
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=False, port=server_port, host="0.0.0.0")
