# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/product/', methods=['GET'])
def product():
    return jsonify({"p_name": '11111'})


if __name__ == '__main__':
    app.run()
