# -*- coding: utf-8 -*-

from app import xor, mobile_info
from flask import Flask, request, jsonify
from publish import uploda

app = Flask(__name__)


@app.route("/xor", methods=["POST"])
def mobile_xor():
    mobile = request.form.get("mobile")
    if mobile:
        return xor(mobile)
    return "xxx"


@app.route("/mobile_info", methods=["POST"])
def get_mobile_info():
    mobile = request.form.get("mobile")
    if mobile:
        return jsonify(mobile_info(mobile))
    return "xxx"


@app.route("/file_path", methods=["POST"])
def file_path():
    return jsonify(uploda().main())


if __name__ == '__main__':
    app.run("0.0.0.0", port=6789)
