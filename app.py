from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    return f"<p>Hello, World! Welcome to {path}</p>"

if __name__ == '__main__':
    app.run()
