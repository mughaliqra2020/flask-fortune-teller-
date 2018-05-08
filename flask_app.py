
# A very simple Flask Hello World app for you to get started with...

from __future__ import print_function
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
#from car_data import get_cars_by  # Week 12 Day 1 Sample Demo code
import json
import sys

app = Flask(__name__)

recipe_data = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="iqram2020",
    password="fun11116",
    hostname="iqram2020.mysql.pythonanywhere-services.com",
    databasename="iqram2020$MyData")

engine = create_engine(recipe_data)

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")

@app.route('/search', methods=["GET"])
def get_fashion():
    search = request.args.get("search")
    # below is how we can print to our error log, will probably remove this once debugging is complete
    sql_query_string, params = create_query(search)
    # below is a good debug line, but will probably remove once debugging is complete
    print("sql_query_string: {0} params: {1}".format(sql_query_string, params), file=sys.stderr)
    # definition for this execute method signature here https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
    results = engine.execute(sql_query_string, params)
    return json.dumps([(dict(row.items())) for row in results])

def create_query(parameter):
    query_string = "SELECT * FROM fashion"
    params = ()
    # we will set convention to always add a space at the BEGINNING of the sql chunk we're adding
    if parameter != "":
        query_string += " WHERE category LIKE %s"
        params += ("%"+parameter+"%",)
    # we're adding this limit to cover the scenario the user didn't supply any
    # paramters. We don't want to return ALL the rows in our DB!
    query_string += " limit 5"

    return query_string, params
