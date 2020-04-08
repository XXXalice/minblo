from flask import Flask
from flask import render_template, request, url_for, jsonify
from .handler import expert as ex
import random

def startup_server():
    app = Flask(__name__) # minblo server

    @app.route('/')
    def index():
        # root page
        pass

    @app.route('/posts/<int:post_num>', methods=['GET'])
    def blogs(post_num):
        return post_num


    @app.route('/ume', methods=['GET'])
    def umemiya():
        expert = ex.Expert(class_id=random.randint(256))


if __name__ == '__main__':
    startup_server()
else:
    import sys
    sys.stdout.write("Can not refer this scripts from other programs. \nplz run directly.")

