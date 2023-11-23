"""
starts a web process
"""
import os
import random

import redis
from flask import Flask, redirect

from cowsay import cowsay, get_random_cow
from shared import consume_cpu, consume_memory

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


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    """
    default catch-all path
    """
    consume_cpu()
    consume_memory()

    status_code = status_codes[random.randint(1, 10)]
    if status_code == 301:
        return redirect("http://www.example.com", code=302)

    cow = get_random_cow()
    message = f"Hello, World! Welcome to /{path} ({status_code})"
    html = f"<pre><code>{cowsay(message, cow=cow)}</code></pre>"
    return html, status_code


@app.route("/redis")
def redis_path():
    """
    tests redis
    """

    host = os.getenv("REDIS_HOST")
    port = int(os.getenv("REDIS_PORT"))
    password = os.getenv("REDIS_PASS")
    connection = redis.Redis(
        host=host, port=port, password=password, decode_responses=True
    )
    connection.set("foo", "bar")
    html = f"<pre><code>{connection.get('foo')}</code></pre>"
    return html, 200


if __name__ == "__main__":
    app.run()
