from flask import Flask
import random

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    some_str = ' ' * (1000000 * random.randint(4, 32))
    return f"<p>Hello, World! Welcome to {path}</p>"

if __name__ == '__main__':
    app.run()
