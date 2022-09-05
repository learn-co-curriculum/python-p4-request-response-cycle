import os

from flask import Flask, request, current_app, g

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.path}</h3>''', \
            202

if __name__ == '__main__':
    app.run()
