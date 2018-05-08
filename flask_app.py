
# A very simple Flask Hello World app for you to get started with...

from __future__ import print_function
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
#from car_data import get_cars_by  # Week 12 Day 1 Sample Demo code
import json
import sys

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")

@app.route('/search', methods=["GET"])
def get_fashion():
    search = request.args.get(string="search")
    # below is how we can print to our error log, will probably remove this once debugging is complete
    sql_query_string, params = create_query(search)
    # below is a good debug line, but will probably remove once debugging is complete
    print("sql_query_string: {0} params: {1}".format(sql_query_string, params), file=sys.stderr)
    # definition for this execute method signature here https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
    results = engine.execute(sql_query_string, params)
    return json.dumps([(dict(row.items())) for row in results])

def create_query(perameter):
    need_or_operator = False
    query_string = "SELECT recipe_name, recipe_link, category FROM RecipeData"
    params = ()
    # we will set convention to always add a space at the BEGINNING of the sql chunk we're adding
    if name != "":
        query_string += " WHERE recipe_name LIKE %s"
        need_or_operator = True
        params += ("%"+name+"%",)
    if category != "":
        if need_or_operator:
            query_string += " OR category = %s"
        else:
            query_string += " WHERE category = %s"
            need_or_operator = True
        params += (category,)
    if url != "":
        if need_or_operator:
            query_string += " OR recipe_link LIKE %s"
        else:
            query_string += " WHERE recipe_link LIKE %s"
        params += ("%"+url+"%",)
    # we're adding this limit to cover the scenario the user didn't supply any
    # paramters. We don't want to return ALL the rows in our DB!
    query_string += " limit 5"

    return query_string, params
