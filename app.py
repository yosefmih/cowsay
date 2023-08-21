from flask import Flask
import concurrent.futures
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

def memory_consumer():
    rand_one = random.randint(16, 32)
    rand_two = random.randint(16, 32)
    foo = ['bar' for _ in range((1000000 * (rand_one + rand_two)))]
    del foo

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    futures = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        futures.append(executor.submit(memory_consumer))
        concurrent.futures.wait(futures)

    status_code = status_codes[random.randint(1, 10)]
    if status_code == 301:
        return redirect("http://www.example.com", code=302)

    return f"<p>Hello, World! Welcome to {path}</p>", status_code

if __name__ == '__main__':
    app.run()
