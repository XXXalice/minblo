from flask import Flask
from flask import render_template, request, url_for, jsonify
from handler import expert as ex
import random

app = Flask(__name__) # minblo server


@app.route('/')
def index():
    # root page
    return "hello!"

@app.route('/posts/<int:post_num>', methods=['GET'])
def blogs(post_num):
    return str(post_num)


@app.route('/ume', methods=['GET'])
def umemiya():
    expert = ex.Expert(class_id=random.randint(256))


def startup_server(debug=True):
    app.run(debug=debug)

if __name__ == '__main__':
    startup_server()
else:
    import sys
    sys.stdout.write("Can not refer this scripts from other programs. \nplz run directly.")
