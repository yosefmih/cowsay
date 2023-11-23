"""
starts a web process
"""
import os
import random
import ssl

import pg8000.native
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
        host=host,
        port=port,
        password=password,
        decode_responses=True,
        ssl=True,
        ssl_cert_reqs="none",
    )
    connection.set("foo", "bar")
    html = f"<pre><code>ping redis with tls: {connection.ping()}</code></pre>"
    return html, 200


@app.route("/postgres")
def postgres_path():
    """
    tests postgres
    """

    host = os.getenv("DB_HOST")
    port = int(os.getenv("DB_PORT"))
    password = os.getenv("DB_PASS")
    username = os.getenv("DB_USER")

    ssl_context = ssl.create_default_context()
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.load_verify_locations("global-bundle.pem")

    con = pg8000.native.Connection(
        user=username, password=password, host=host, port=port, ssl_context=ssl_context
    )
    for row in con.run("SELECT 1"):
        html = f"<pre><code>connect to postgres with ssl: {row}</code></pre>"

    con.close()
    return html, 200


if __name__ == "__main__":
    app.run()
