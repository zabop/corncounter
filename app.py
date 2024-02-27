"""
A sample Hello World server.
"""
import os

from flask import Flask

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    return "It's up."

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
