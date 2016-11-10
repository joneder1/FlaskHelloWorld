from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return render_template('template.html', name="World")

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('template.html', name=name)

#decided to pass this to template2.html so I could use the Darth Vader jpg
@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname, lastname):
    name = lastname[:3] + firstname[:2]
    return render_template('template2.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
    
