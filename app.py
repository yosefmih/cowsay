from flask import Flask
import random

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    rand_one = random.randint(1, 16)
    rand_two = random.randint(1, 16)
    some_str = ' ' * (1000000 * (rand_one + rand_two))
    return f"<p>Hello, World! Welcome to {path}</p>"

if __name__ == '__main__':
    app.run()
