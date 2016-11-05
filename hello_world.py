from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())  

@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname, lastname):
    firstname = firstname[:2]
    lastname = lastname[:3]
    html = """
        <h1>
            Hello Jedi {0}{1}!
        </h1>
        <p>
            Here's a picture of your father.  Awww...
        </p>
        <img src="https://upload.wikimedia.org/wikipedia/en/7/76/Darth_Vader.jpg">
    """
    return html.format(lastname.title(), firstname.title())    

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            
