from flask import Flask
import random

app = Flask(__name__)

status_codes = {
    1: 100,
    2: 200,
    3: 201,
    4: 202,
    5: 200,
    6: 200,
    7: 200,
    8: 302,
    9: 404,
    10: 500,
}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    status_code = status_codes[random.randint(1, 10)]

    rand_one = random.randint(1, 16)
    rand_two = random.randint(1, 16)
    some_str = ' ' * (1000000 * (rand_one + rand_two))
    del some_str

    if status_code == 301:
        return redirect("http://www.example.com", code=302)

    return f"<p>Hello, World! Welcome to {path}</p>", status_code

if __name__ == '__main__':
    app.run()
