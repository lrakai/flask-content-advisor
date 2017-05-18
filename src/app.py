'''An advisor on what content type to try'''
from flask import Flask
from random import randint
app = Flask(__name__)

content = ['learning path', 'lab', 'course', 'quiz']


@app.route('/')
def hello_world():
    return 'How about trying a ' + content[randint(0,2)] + ' next'
