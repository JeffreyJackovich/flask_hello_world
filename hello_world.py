from flask import Flask
from os import environ
import functools

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

def twist(twister):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print twister
            function(*args, **kwargs)
        return wrapper
    return decorator

@twist("She sells sea shells")
def spoon():
    print "A well-boild icile"
    
@app.route("/hello/<name>")
def hi_persoon(name):
    return "Hello {}!".format(name.title())
    
@app.route("/hello/<name>")
#def hello_person(name):
 #   html = """
 #       <h1>
 #           Hello {}!
 #       </h1>
 #       <p>
 #           Here's a picture of a kitten.  Awww
 #       </p>
 #       <img src="http://placekitten.com/g/200/300">
  #  """
 #   return html.format(name.title())
    
@app.route("/jedi/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))
