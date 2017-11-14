# run a rest api which starts a new thread to each request

import thread
from flask import Flask

app = Flask(__name__)

def print_time(thread_name):
    print thread_name


@app.route("/new", methods=['POST'])
def new():
    pass


@app.route("/update")
def update():
    pass


@app.route("/all")
def get_all():
    pass


@app.route("/<name>")
def get(name):
    try:
        thread.start_new_thread(print_time, ("Thread-1",))
    except:
        return "Error: unable to start thread"
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
