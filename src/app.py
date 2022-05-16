from flask import Flask, jsonify, render_template
import socket


app = Flask(__name__)



def fetch_details():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)


@app.route('/')
def index():
    return "<p>Hello first endpoint</p>"


@app.route("/health")
def health():
    return jsonify(status="pong")


@app.route("/details")
def details():
    hostname, ip = fetch_details()
    return render_template("index.html", hostname=hostname, ip=ip)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)