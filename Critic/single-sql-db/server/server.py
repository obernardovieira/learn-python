from flask import Flask, request
import json
import mysql.connector

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

    try:
        cnx = mysql.connector.connect(user='scott', database='testt')
    except mysql.connector.Error as err:
        print(err)
    else:
        cnx.close()

    app.run(host="0.0.0.0", port=3000, threaded=True)
