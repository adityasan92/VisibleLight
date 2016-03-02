from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse
import logging
import sys

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
