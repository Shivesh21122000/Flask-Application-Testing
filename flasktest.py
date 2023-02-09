from flask import Flask
import threading
import tkinterTest
# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask(__name__)

thread = threading.Thread(target = tkinterTest.flaskFun, args=[])
thread.start()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()