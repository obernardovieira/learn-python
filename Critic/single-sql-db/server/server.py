import os
from flask import Flask, request
import json
import mysql.connector
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
cnx = ""


@app.route("/new", methods=['POST'])
def new():
    if not request.json:
        return json.dumps({"result": "400"})

    data = json.load(request.json)
    add_employee = ("INSERT INTO client(firstname, lastname, address, status, animal, car) VALUES" +
                    "(%(firstname)s, %(lastname)s, %(address)s, %(status)s, %(animal)s, %(car)s)")
    data_employee = (data["firstname"], data["lastname"],
                    data["address"], data["status"], data["animal"], data["car"])
    cursor = cnx.cursor()
    cursor.execute(add_employee, data_employee)
    return json.dumps({"result": "200"})


@app.route("/update")
def update():
    pass


@app.route("/all")
def get_all():
    pass


@app.route("/<name>")
def get(name):
    pass


if __name__ == "__main__":

    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASS = os.environ.get("MYSQL_PASS")
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_DB = os.environ.get("MYSQL_DB")

    try:
        cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASS,
                                      host=MYSQL_HOST, database=MYSQL_DB)
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()

    app.run(host="0.0.0.0", port=3000, threaded=True)
